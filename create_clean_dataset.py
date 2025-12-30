import pandas as pd
import requests
import time

API_KEY = "dd85adcf16df56383c95fb7562f63f42"
BASE_URL = "https://api.themoviedb.org/3"

# Classic + Popular Hollywood and Bollywood movies
ESSENTIAL_MOVIES = [
    # Classics - Hollywood
    (603, "hollywood"),      # The Matrix
    (550, "hollywood"),      # Fight Club
    (27205, "hollywood"),    # Inception
    (157336, "hollywood"),   # Interstellar
    (155, "hollywood"),      # The Dark Knight
    
    # Popular - Hollywood
    (278, "hollywood"),      # The Shawshank Redemption
    (238, "hollywood"),      # The Godfather
    (240, "hollywood"),      # The Godfather Part II
    (129, "hollywood"),      # Spirited Away
    (24, "hollywood"),       # Kill Bill Vol 1
    
    # Popular - Bollywood
    (19404, "bollywood"),    # 3 Idiots
    (20453, "bollywood"),    # PK
    (254128, "bollywood"),   # Bajrangi Bhaijaan
    (445595, "bollywood"),   # Andhadhun
    (19359, "bollywood"),    # Rang De Basanti
]

def fetch_movie_data(movie_id):
    """Fetch movie details from TMDB"""
    try:
        url = f"{BASE_URL}/movie/{movie_id}"
        params = {
            "api_key": API_KEY,
            "append_to_response": "credits,keywords"
        }
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  Error fetching movie {movie_id}: {e}")
        return None

movies_data = []
seen_ids = set()

print("Fetching essential movies...")

for movie_id, industry in ESSENTIAL_MOVIES:
    # Avoid duplicates
    if movie_id in seen_ids:
        continue
        
    print(f"Fetching {movie_id}...", end=" ")
    d = fetch_movie_data(movie_id)
    
    if not d:
        print("❌ Failed")
        continue
    
    # Extract features
    genres = " ".join(g["name"] for g in d.get("genres", []))
    cast = " ".join(c["name"] for c in d.get("credits", {}).get("cast", [])[:5])
    keywords = " ".join(k["name"] for k in d.get("keywords", {}).get("keywords", []))
    
    features = f"{genres} {cast} {keywords} {industry}".lower()
    
    movies_data.append({
        "id": d["id"],
        "title": d["title"],
        "industry": industry,
        "features": features
    })
    
    seen_ids.add(d["id"])
    print("✅")
    time.sleep(0.5)

df = pd.DataFrame(movies_data)

# Remove any duplicate IDs (keep first occurrence)
df = df.drop_duplicates(subset=['id'], keep='first')

df.to_csv("data/movies.csv", index=False)

print(f"\n✅ Dataset created with {len(df)} movies")
print(f"Hollywood: {len(df[df['industry']=='hollywood'])}")
print(f"Bollywood: {len(df[df['industry']=='bollywood'])}")

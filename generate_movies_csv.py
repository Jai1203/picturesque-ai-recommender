import requests
import pandas as pd
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API_KEY = "dd85adcf16df56383c95fb7562f63f42"
BASE_URL = "https://api.themoviedb.org/3"

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503])
session.mount("https://", HTTPAdapter(max_retries=retries))

movies_data = []

# Bollywood + Hollywood discovery
DISCOVER_URLS = [
    # Hollywood
    {
        "language": "en-US",
        "region": "US",
        "with_original_language": "en",
        "industry": "hollywood"
    },
    # Bollywood
    {
        "language": "hi-IN",
        "region": "IN",
        "with_original_language": "hi",
        "industry": "bollywood"
    }
]

def fetch_movies(params, page):
    params["api_key"] = API_KEY
    params["page"] = page
    r = session.get(f"{BASE_URL}/discover/movie", params=params, timeout=10)
    r.raise_for_status()
    return r.json()["results"]

def fetch_details(movie_id):
    r = session.get(
        f"{BASE_URL}/movie/{movie_id}",
        params={"api_key": API_KEY, "append_to_response": "credits,keywords"},
        timeout=10
    )
    r.raise_for_status()
    return r.json()

print("Building mixed Bollywood + Hollywood dataset...")

for config in DISCOVER_URLS:
    for page in range(1, 8):  # ~140 movies per industry
        movies = fetch_movies({
            "language": config["language"],
            "region": config["region"],
            "with_original_language": config["with_original_language"]
        }, page)

        for m in movies:
            try:
                d = fetch_details(m["id"])

                genres = " ".join(g["name"] for g in d.get("genres", []))
                cast = " ".join(c["name"] for c in d.get("credits", {}).get("cast", [])[:5])
                keywords = " ".join(k["name"] for k in d.get("keywords", {}).get("keywords", []))

                features = f"""
                {genres} {cast} {keywords}
                {config['industry']} {config['region']} {config['with_original_language']}
                """.lower()

                movies_data.append({
                    "id": m["id"],
                    "title": m["title"],
                    "industry": config["industry"],
                    "features": features
                })

                time.sleep(0.4)

            except Exception:
                continue

df = pd.DataFrame(movies_data)
df.to_csv("data/movies.csv", index=False)

print(f"✅ Dataset created with {len(df)} movies")

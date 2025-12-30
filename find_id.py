import requests

API_KEY = "dd85adcf16df56383c95fb7562f63f42"
r = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key": API_KEY, "query": "Andhadhun"})
for m in r.json()["results"][:5]:
    print(f"ID: {m['id']}, Title: {m['title']}, Release: {m.get('release_date', 'N/A')}")

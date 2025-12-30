import json
import os
from datetime import datetime

MEMORY_FILE = "data/user_memory.json"

def _load():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_user(user_id: str):
    data = _load()
    return data.get(user_id, {
        "user_id": user_id,
        "history": [],
        "wrapped": []
    })

def update_history(user_id: str, movie_ids: list):
    data = _load()
    user = get_user(user_id)

    user["history"].append({
        "liked_movie_ids": movie_ids,
        "timestamp": datetime.utcnow().isoformat()
    })

    data[user_id] = user
    _save(data)

def save_wrapped(user_id: str, wrapped_data: dict):
    data = _load()
    user = get_user(user_id)

    wrapped_entry = {
        "id": wrapped_data.get("id"),
        "timestamp": datetime.utcnow().isoformat(),
        "data": wrapped_data
    }

    user["wrapped"].append(wrapped_entry)
    data[user_id] = user
    _save(data)

def get_wrapped_by_id(wrapped_id: str):
    data = _load()
    for user in data.values():
        for wrapped in user.get("wrapped", []):
            if wrapped["id"] == wrapped_id:
                return wrapped
    return None
def get_wrapped_by_id(wrapped_id: str):
    data = _load()
    for user in data.values():
        for w in user["wrapped"]:
            if w["data"]["id"] == wrapped_id:
                return w
    return None

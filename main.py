from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from recommender import MovieRecommender
from user_memory import update_history, save_wrapped, get_wrapped_by_id

app = FastAPI(title="Picturesque Recommendation API")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://picturesque.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

recommender = MovieRecommender("data/movies.csv")


# ---------- MODELS ----------
class RecommendRequest(BaseModel):
    liked_movie_ids: List[int]
    user_id: str


class WrappedSaveRequest(BaseModel):
    user_id: str
    wrapped: dict


# ---------- ROUTES ----------
@app.get("/")
def root():
    return {
        "status": "Picturesque backend running",
        "endpoints": [
            "/recommend",
            "/wrapped/save",
            "/wrapped/{id}",
            "/docs"
        ]
    }


@app.post("/recommend")
def recommend_movies(req: RecommendRequest):
    update_history(req.user_id, req.liked_movie_ids)
    recommendations = recommender.recommend(req.liked_movie_ids)
    return {"recommendations": recommendations}


@app.post("/wrapped/save")
def save_wrapped_snapshot(req: WrappedSaveRequest):
    save_wrapped(req.user_id, req.wrapped)
    return {"status": "saved"}


@app.get("/wrapped/{wrapped_id}")
def get_public_wrapped(wrapped_id: str):
    wrapped = get_wrapped_by_id(wrapped_id)
    if not wrapped:
        raise HTTPException(status_code=404, detail="Wrapped not found")
    return wrapped

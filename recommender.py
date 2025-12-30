import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import random


class MovieRecommender:
    def __init__(self, csv_path: str):
        self.df = pd.read_csv(csv_path)

        # ---- CLEAN DATA ----
        self.df["features"] = self.df["features"].fillna("")
        self.df["industry"] = self.df["industry"].fillna("unknown")
        self.df["title"] = self.df["title"].fillna("")

        # REMOVE SENTIMENT NOISE
        self.df = self.df[
            ~self.df["title"].str.lower().isin(
                {"positive", "negative", "neutral"}
            )
        ].reset_index(drop=True)

        # ---- VECTORIZE ----
        self.feature_matrix = self._vectorize(self.df["features"])
        self.similarity = cosine_similarity(self.feature_matrix)

        self.id_to_index = {
            int(movie_id): idx
            for idx, movie_id in enumerate(self.df["id"].values)
        }

    def _vectorize(self, texts):
        vocab = {}
        vectors = []

        for text in texts:
            vec = {}
            for word in text.lower().split():
                vec[word] = vec.get(word, 0) + 1
                vocab[word] = True
            vectors.append(vec)

        vocab = list(vocab.keys())
        matrix = np.zeros((len(texts), len(vocab)))

        for i, vec in enumerate(vectors):
            for j, word in enumerate(vocab):
                matrix[i, j] = vec.get(word, 0)

        return matrix

    def _industry_weight(self, movie_industry, liked_industries):
        return 1.0 if movie_industry in liked_industries else 0.7

    def recommend(self, liked_movie_ids, top_n=12):
        liked_movie_ids = list(set(map(int, liked_movie_ids)))
        if not liked_movie_ids:
            return []

        # ---- BUILD USER TASTE VECTOR ----
        liked_indices = [
            self.id_to_index[mid]
            for mid in liked_movie_ids
            if mid in self.id_to_index
        ]

        if not liked_indices:
            return []

        taste_vector = np.mean(self.feature_matrix[liked_indices], axis=0)
        taste_vector = taste_vector.reshape(1, -1)

        # ---- SIMILARITY ----
        sim_scores = cosine_similarity(taste_vector, self.feature_matrix)[0]

        liked_industries = set(
            self.df[self.df["id"].isin(liked_movie_ids)]["industry"]
        )

        scored = []
        for i, score in enumerate(sim_scores):
            movie = self.df.iloc[i]
            movie_id = int(movie["id"])

            if movie_id in liked_movie_ids:
                continue

            if score < 0.02:
                continue

            weight = self._industry_weight(
                movie["industry"], liked_industries
            )

            scored.append((movie_id, score * weight, i))

        # ---- SORT BY SCORE ----
        scored.sort(key=lambda x: x[1], reverse=True)

        # ---- TAKE TOP CANDIDATES (CRITICAL FIX) ----
        TOP_POOL_SIZE = min(50, len(scored))
        top_pool = scored[:TOP_POOL_SIZE]

        # ---- DIVERSITY-AWARE RANDOM SAMPLING ----
        random.shuffle(top_pool)

        results = []
        used_indices = []

        for movie_id, base_score, idx in top_pool:
            penalty = 1.0
            for used_idx in used_indices:
                sim = cosine_similarity(
                    self.feature_matrix[idx].reshape(1, -1),
                    self.feature_matrix[used_idx].reshape(1, -1),
                )[0][0]
                penalty *= (1 - sim)

            final_score = base_score * penalty

            # Light randomness
            final_score *= random.uniform(0.85, 1.15)

            results.append((movie_id, final_score, idx))

            if len(results) >= top_n:
                break

        # ---- FINAL SORT ----
        results.sort(key=lambda x: x[1], reverse=True)

        output = []
        for movie_id, _, _ in results:
            movie = self.df[self.df["id"] == movie_id].iloc[0]
            output.append({
                "id": int(movie["id"]),
                "title": movie["title"],
                "industry": movie["industry"],
            })

        return output

# 🎬 Picturesque – AI Movie Recommendation & Wrapped Experience

Picturesque is a full-stack AI-powered movie recommendation system that analyzes user taste and generates a personalized **“Wrapped” experience** — similar to Spotify Wrapped — with shareable and downloadable insights.

This project focuses on **recommendation logic, data-driven personalization, and product-style UX**, built end-to-end by a single developer.

---

## 🚀 Features

- 🎥 AI-based movie recommendations using cosine similarity
- 🧠 Taste profiling from user-selected movies
- 🎁 Personalized “Picturesque Wrapped” dashboard
- 🔗 Shareable Wrapped links (`/wrapped/[id]`)
- 📸 Download Wrapped as an image
- 📊 Genre, actor, mood & industry breakdowns
- 🗂 Persistent user history & Wrapped snapshots (JSON-based)

---

## 🧱 Architecture

### Frontend
- **Next.js (App Router)**
- **TypeScript**
- **Tailwind CSS**
- Client-side data fetching & visualization

### Backend
- **FastAPI (Python)**
- **Scikit-learn**
- Lightweight JSON-based persistence (no database)

> ⚠️ Note: The backend exists at the project root and is not inside a separate `backend/` folder.

---

## 🔄 Data Flow

User selects movies
↓
Frontend (Next.js)
↓
FastAPI Recommendation API
↓
ML Recommendation Engine
↓
TMDB Metadata Enrichment
↓
Wrapped Dashboard + Shareable Link


---

## 🤖 Recommendation Logic

- Movies are vectorized using textual feature data
- A **user taste vector** is computed as the mean of liked movie vectors
- Similarity is calculated using **cosine similarity**
- Industry-based weighting (Hollywood / Bollywood preference)
- Diversity-aware sampling avoids repetitive recommendations

---

## 🎁 Wrapped Feature

Each **Picturesque Wrapped** includes:

- Total number of recommendations
- Industry split (Hollywood vs Bollywood)
- Genre distribution (visualized)
- Top actors the user “vibes with”
- Mood breakdown
- Downloadable image version
- Public, read-only shareable URL

Example:


/wrapped/c17117b4-ba23-4b4c-9f54-f1657ba9f7f2


---

## 🛠 Local Setup & Running the Project

### 1️⃣ Backend (FastAPI)

The backend runs from the **project root**.

#### Activate virtual environment (Windows PowerShell):
```powershell
C:/Users/amitt/OneDrive/Desktop/Picturesque/venv/Scripts/Activate.ps1

Start FastAPI server:
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

2️⃣ Frontend (Next.js)
cd frontend
npm install
npm run dev


Frontend runs at:

http://localhost:3000

🧪 Tech Stack Summary
Layer	Technology
Frontend	Next.js, TypeScript, Tailwind CSS
Backend	FastAPI, Python
ML	Scikit-learn, Cosine Similarity
Storage	JSON-based persistence
APIs	TMDB (movie metadata)
🎯 Project Goals

Demonstrate real-world recommendation system logic

Showcase full-stack integration

Build a product-style user experience

Create something shareable and explainable in interviews

👨‍💻 Author

Jai Chadha
Aspiring Software Engineer
Interested in Full-Stack Development, Machine Learning & Product Engineering


---

## ✅ What to Do Next (Final Steps)

```bash
git add README.md
git commit -m "Update README to match local project setup"
git push

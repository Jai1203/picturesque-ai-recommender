# 🎬 Picturesque – AI Movie Recommendation & Wrapped Experience

Picturesque is a full-stack AI-powered movie recommendation system that analyzes user taste and generates a personalized “Wrapped” experience — similar to Spotify Wrapped — with shareable and downloadable insights.

---

## 🚀 Features

- 🎥 AI-based movie recommendations using cosine similarity
- 🧠 Taste profiling from user-selected movies
- 🎁 Personalized “Picturesque Wrapped” dashboard
- 🔗 Shareable Wrapped links (`/wrapped/[id]`)
- 📸 Download Wrapped as an image
- 📊 Genre, actor, mood & industry breakdowns
- 🗂 Persistent user history & snapshots

---

## 🧱 Architecture

### Frontend
- **Next.js (App Router)**
- **TypeScript**
- **Tailwind CSS**
- Hosted on **Vercel**

### Backend
- **FastAPI (Python)**
- **Scikit-learn**
- Hosted on **Render**

### Data Flow
User selects movies
↓
Frontend → FastAPI API
↓
ML recommendation engine
↓
Enriched TMDB metadata
↓
Wrapped dashboard + shareable link


---

## 🤖 Recommendation Logic

- Movies are vectorized using textual features
- User taste vector = mean of liked movie vectors
- Similarity computed via **cosine similarity**
- Industry weighting applied (Hollywood/Bollywood bias)
- Diversity-aware sampling avoids repetitive recommendations

---

## 🎁 Wrapped Feature

Each Wrapped includes:
- Total recommendations
- Industry split
- Genre distribution (pie chart)
- Favorite actors
- Mood breakdown
- Downloadable image
- Public shareable URL

Example:


/wrapped/c17117b4-ba23-4b4c-9f54-f1657ba9f7f2


---

## 🌍 Deployment

| Layer | Platform |
|------|---------|
| Frontend | Vercel |
| Backend | Render |

---

## 🛠 Local Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Frontend
cd frontend
npm install
npm run dev

👨‍💻 Author

Jai Chadha
Aspiring Software Engineer | ML & Full-Stack Enthusiast


Then commit:

```bash
git add README.md
git commit -m "Add professional README"
git push

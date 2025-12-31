
# 🎬 Picturesque – AI Movie Recommendation & Wrapped Experience

Picturesque is a full-stack AI-powered movie recommendation system that analyzes user taste and generates a personalized **“Wrapped” experience** — inspired by Spotify Wrapped — with shareable and downloadable insights.

This project focuses on **recommendation logic, data-driven personalization, and product-style UX**, built end-to-end by a single developer.

https://github.com/user-attachments/assets/e2a725bd-b3d8-4bd8-95be-91c4aa68a3ce


<img width="1916" height="931" alt="Screenshot 2025-12-31 224251" src="https://github.com/user-attachments/assets/f151f78f-e11f-4656-b475-503c3b882631" />
<img width="1919" height="762" alt="Screenshot 2025-12-31 224234" src="https://github.com/user-attachments/assets/d44c796d-41e4-4bb9-80eb-79f1d7ec7604" />
<img width="1919" height="945" alt="Screenshot 2025-12-31 224224" src="https://github.com/user-attachments/assets/581fbb87-da9d-45e5-bb4b-5c0ba2356f8a" />
<img width="1919" height="938" alt="Screenshot 2025-12-31 224147" src="https://github.com/user-attachments/assets/dc375284-8d2e-4004-8f0f-88c7fd201d80" />

<img width="2432" height="2624" alt="picturesque-wrapped(42)" src="https://github.com/user-attachments/assets/a8a438d9-748c-428c-a544-70a03bee6994" />
<img width="2432" height="2624" alt="picturesque-wrapped(41)" src="https://github.com/user-attachments/assets/d1cbe1f2-5eec-4f3f-bcd1-bbb5b2150c7a" />
<img width="2432" height="2624" alt="picturesque-wrapped(40)" src="https://github.com/user-attachments/assets/78751fba-bcef-4e7b-81d8-0101c4162e17" />
<img width="2432" height="2624" alt="picturesque-wrapped(39)" src="https://github.com/user-attachments/assets/f3fe5239-6ed6-4eeb-87c0-607b5c17da44" />
<img width="2432" height="2624" alt="picturesque-wrapped(38)" src="https://github.com/user-attachments/assets/1431585f-3395-4d71-b357-87563b56c69e" />
<img width="2432" height="2624" alt="picturesque-wrapped(37)" src="https://github.com/user-attachments/assets/384fd744-9bd5-466e-9f34-ae082da2ff82" />
<img width="2432" height="2624" alt="picturesque-wrapped(36)" src="https://github.com/user-attachments/assets/f49a4d20-1deb-484d-b789-414d98768bc1" />


---

## 🚀 Features

- 🎥 AI-based movie recommendations using **cosine similarity**
- 🧠 Taste profiling from user-selected movies
- 🎁 Personalized **Picturesque Wrapped** dashboard
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
- Client-side data fetching & visualizations (Recharts)
- Wrapped image export using `html-to-image`

### Backend
- **FastAPI (Python)**
- **Scikit-learn**
- Lightweight **JSON-based persistence** (no database)

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
- **Diversity-aware sampling** avoids repetitive recommendations

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

Activate virtual environment:

```bash
venv/Scripts/Activate.ps1

Start the FastAPI server:

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

# ✅ GIT COMMANDS (COPY–PASTE)

Run these **from your project root**:

```bash
git status
git add README.md
git commit -m "Update README to reflect project architecture and features"
git push


https://github.com/user-attachments/assets/9698a5ff-0227-488a-8250-2a3bc56821b0


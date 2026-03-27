from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from news_engine import fetch_news

app = FastAPI()

# 🔥 CORS FIX (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "TruthLens API running"}

@app.get("/news")
def get_news():
    try:
        news = fetch_news()  # ✅ NO ARGUMENT
        return news
    except Exception as e:
        return {"error": str(e), "message": "Failed to fetch news"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from news_engine import fetch_news

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ROOT TEST
@app.get("/")
def home():
    return {"message": "TruthLens Backend Running 🚀"}

# ✅ NEWS ROUTE (THIS WAS MISSING OR WRONG)
@app.get("/news")
def get_news():
    return fetch_news()
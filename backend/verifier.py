import requests
from config import NEWS_API_KEY

def clean_title(title):
    words = title.split()
    return " ".join(words[:6])


def verify_news(title):

    query = clean_title(title) + " news"

    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=relevancy&pageSize=20&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    data = response.json()

    sources = set()

    # 🔹 MAIN LOOP
    for a in data.get("articles", []):
        source_name = a["source"]["name"]

        if source_name:
            sources.add(source_name.strip())

    # 🔥 ADD YOUR FALLBACK HERE 👇
    if not sources:
        query = title.split()[0] + " news"

        url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=10&apiKey={NEWS_API_KEY}"

        response = requests.get(url)
        data = response.json()

        for a in data.get("articles", []):
            source_name = a["source"]["name"]
            if source_name:
                sources.add(source_name.strip())

    # 🔹 RETURN MUST BE LAST
    return list(sources)
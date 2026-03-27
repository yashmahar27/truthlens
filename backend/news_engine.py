import feedparser
import time
import random

# 🔥 CACHE SYSTEM
CACHE = {"data": [], "timestamp": 0}
CACHE_DURATION = 300  # 5 min

# 🌍 RSS SOURCES
RSS_FEEDS = [
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.skynews.com/feeds/rss/home.xml",
    "https://www.thehindu.com/news/national/feeder/default.rss",
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
]

# 🧠 LIGHT AI (UPGRADED — WITH MATCHED SOURCES)
def ai_score(title, all_titles):

    title_words = set(title.lower().split())

    similar_count = 0
    matched_titles = []

    for t in all_titles:
        words = set(t.lower().split())
        common = title_words.intersection(words)

        if len(common) >= 3:
            similar_count += 1
            matched_titles.append(t)

    # 🔥 SAME SCORING (UNCHANGED LOGIC)
    if similar_count >= 8:
        score = 90
    elif similar_count >= 5:
        score = 75
    elif similar_count >= 3:
        score = 60
    elif similar_count >= 1:
        score = 45
    else:
        score = 30

    if score >= 75:
        status = "Verified"
    elif score >= 50:
        status = "Medium Trust"
    else:
        status = "Low Trust"

    reason = f"{similar_count} sources reported similar news"

    return score, status, reason, matched_titles[:5]  # ✅ NEW


# 📰 CATEGORY DETECTION (UNCHANGED)
def detect_category(title):
    t = title.lower()

    if "election" in t or "government" in t or "minister" in t or "policy" in t:
        return "Politics"
    elif "cricket" in t or "football" in t or "match" in t or "tournament" in t:
        return "Sports"
    elif "ai" in t or "technology" in t or "tech" in t or "startup" in t:
        return "Technology"
    elif "market" in t or "economy" in t or "business" in t:
        return "Business"
    else:
        return "General"


# 🚀 MAIN FUNCTION (MINIMAL CHANGES)
def fetch_news():

    if time.time() - CACHE["timestamp"] < CACHE_DURATION and CACHE["data"]:
        print("USING CACHE")
        return CACHE["data"]

    print("FETCHING NEWS FROM RSS")

    articles = []
    all_titles = []

    # 🔥 COLLECT TITLES
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:15]:
            if entry.get("title"):
                all_titles.append(entry.title)

    # 🔥 PROCESS NEWS
    for feed_url in RSS_FEEDS:
        print("Fetching:", feed_url)

        feed = feedparser.parse(feed_url)

        print("Entries found:", len(feed.entries))

        for i, entry in enumerate(feed.entries[:15]):

            title = entry.get("title", "No Title")

            image = f"https://picsum.photos/400/200?random={random.randint(1,1000)}"

            # ✅ UPDATED CALL
            score, status, reason, matched_titles = ai_score(title, all_titles)

            articles.append({
                "id": f"{i}-{random.randint(1,10000)}",
                "title": title,
                "source": feed.feed.get("title", "Unknown"),
                "url": entry.get("link", ""),
                "image": image,
                "description": entry.get("summary", "No description available"),
                "date": entry.get("published", "No date"),
                "credibility_score": score,
                "status": status,
                "reason": reason,
                "matched_titles": matched_titles,  # ✅ NEW FIELD
                "category": detect_category(title)
            })

    # 🔥 SORT (UNCHANGED)
    articles.sort(key=lambda x: x["credibility_score"], reverse=True)

    CACHE["data"] = articles
    CACHE["timestamp"] = time.time()

    return articles


# 🔍 TEST
if __name__ == "__main__":
    news = fetch_news()
    print("TOTAL NEWS:", len(news))
    for n in news[:5]:
        print(n["title"], "→", n["status"], n["credibility_score"])
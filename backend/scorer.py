TRUSTED_SOURCES = [
    "BBC News",
    "Reuters",
    "The Hindu",
    "NDTV",
    "Indian Express",
    "Al Jazeera English",
    "Bloomberg",
    "NPR",
    "The Times of India",
    "BusinessLine",
    "Economic Times",
    "Hindustan Times",
    "CNN",
    "The Guardian"
]

GOV_SOURCES = [
    "Press Information Bureau",
    "PIB India",
    "india.gov.in",
    "data.gov.in",
    "WHO",
    "United Nations",
]

def calculate_score(sources):

    if not sources:
        return 10

    trusted_count = 0
    gov_bonus = 0

    for s in sources:
        if s in TRUSTED_SOURCES:
            trusted_count += 1

        if s in GOV_SOURCES:
            gov_bonus += 20   # 🔥 strong boost

    base_score = (trusted_count / len(sources)) * 70 + 20

    total_score = base_score + gov_bonus

    return min(round(total_score, 2), 100)

def get_status(score):

    if score > 70:
        return "Verified"
    elif score > 40:
        return "Medium Trust"
    else:
        return "Low Trust"


# TEST
if __name__ == "__main__":
    test_sources = ['Reuters', 'BBC News', 'RandomBlog']

    score = calculate_score(test_sources)
    status = get_status(score)

    print("Score:", score)
    print("Status:", status)
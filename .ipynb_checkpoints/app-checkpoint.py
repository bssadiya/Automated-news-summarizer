from flask import Flask, render_template, request
import requests
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# Function to summarize text using NLP
def summarize_text(text):
    if text:
        # Limiting text to 1024 characters for the summarizer
        summary = summarizer(text[:1024], max_length=60, min_length=20, do_sample=False)
        return summary[0]['summary_text']
    else:
        return "No description available."

# Function to get news data from an API
def get_news(category="general", page=1):
    api_key = "YOUR_API_KEY"
    url = f"https://newsapi.org/v2/top-headlines?category={category}&page={page}&pageSize=10&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])

    # Summarize each article's description
    for article in articles:
        article['summary'] = summarize_text(article.get('description', ""))

    return articles

@app.route("/")
def index():
    category = request.args.get("category", "general")
    page = int(request.args.get("page", 1))
    news_articles = get_news(category, page)
    return render_template("index.html", news_articles=news_articles, category=category, page=page)

if __name__ == "__main__":
    app.run(debug=True)

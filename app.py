from flask import Flask, render_template, request
import requests
from transformers import pipeline
import os
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # hides TF logs

app = Flask(__name__)

# Model 
try:
    summarizer = pipeline("summarization")  # default model
except Exception as e:
    print("❌ Summarizer pipeline failed:", e)
    summarizer = None

# Helper Functions 
def summarize_text(text):
    if text:
        if summarizer:
            try:
                summary = summarizer(text[:1024], max_length=60, min_length=20, do_sample=False)
                return summary[0]['summary_text']
            except Exception:
                pass
        return text  # fallback to original text
    return "No description available."

def evaluate_summary(reference, generated):
    results = {}
    if reference and generated:
        # BLEU
        reference_tokens = [reference.split()]
        generated_tokens = generated.split()
        results['bleu'] = sentence_bleu(reference_tokens, generated_tokens)

        # ROUGE
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
        rouge_scores = scorer.score(reference, generated)
        results['rouge1'] = rouge_scores['rouge1'].fmeasure
        results['rougeL'] = rouge_scores['rougeL'].fmeasure
    return results

#  Categories 
CATEGORIES = ["general", "business", "entertainment", "health", "science", "sports", "technology", "politics"]

#  Safe Request 
def safe_request(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get("articles", [])
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
    # fallback sample data
    return [{"title": "Sample News", "description": "Sample description.", "summary": "Sample description."}]

#  News Fetch 
API_KEY = "41720d26e28a460ba1ca9d8772ee1dac"

def get_news(category="general", page=1):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&page={page}&pageSize=10&apiKey={API_KEY}"
    articles = safe_request(url)
    
    for article in articles:
        description = article.get('description', "")
        summary = summarize_text(description)
        article['summary'] = summary
        if description != summary:
            article['evaluation'] = evaluate_summary(description, summary)
        else:
            article['evaluation'] = None

    return articles

# def get_news_for_search(query, page=1):
#     url = f"https://newsapi.org/v2/everything?q={query}&page={page}&pageSize=10&apiKey={API_KEY}"
#     articles = safe_request(url)
    
#     for article in articles:
#         description = article.get('description', "")
#         summary = summarize_text(description)
#         article['summary'] = summary
#         if description != summary:
#             article['evaluation'] = evaluate_summary(description, summary)
#         else:
#             article['evaluation'] = None

#     return articles


def get_news_for_search(query, page=1):
    url = f"https://newsapi.org/v2/everything?q={query}&page={page}&pageSize=10&apiKey={API_KEY}"
    articles = safe_request(url)
    for article in articles:
        description = article.get('description', "")
        summary = summarize_text(description)
        article['summary'] = summary
        article['evaluation'] = evaluate_summary(description, summary) if description != summary else None
    return articles

#  Routes 
@app.route("/")
def index():
    category = request.args.get("category", "general")  # read query param
    page = int(request.args.get("page", 1))
    news_articles = get_news(category, page)
    return render_template("index.html", news_articles=news_articles, category=category, categories=CATEGORIES, page=page)

@app.route("/about")
def about():
    return render_template("about.html", categories=CATEGORIES)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("q", "")
    page = int(request.args.get("page", 1))
    news_articles = get_news_for_search(query, page) if query else []
    return render_template("search.html", news_articles=news_articles, query=query, categories=CATEGORIES, page=page)

# Run App
if __name__ == "__main__":
    try:
        app.run(debug=True, port=5000)
    except Exception as e:
        print("❌ Flask failed to start:", e)

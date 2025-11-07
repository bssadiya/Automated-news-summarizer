***Automated News Summarizer****
This project is a Flask-based web application that gathers the latest news from different categories and generates short, 
AI-driven summaries for each article. It also evaluates how accurate and meaningful each summary is by comparing it with the original description using BLEU and ROUGE scores. 
The idea behind this project is to make news consumption quicker and smarter by giving readers the key points without needing to read the full article.

***What the project does***

-Fetches live news articles in real time using NewsAPI.org

-Uses a Transformer model to generate concise summaries automatically

-Evaluates each summary using BLEU and ROUGE metrics

-Allows users to search for specific topics or categories

-Handles missing or incomplete data gracefully with fallback content

***Tools and Technologies***

Python (Flask) – for building the backend web framework

Hugging Face Transformers – for AI-powered text summarization

NLTK and ROUGE Score – to evaluate the quality of generated summaries

News API – for fetching the latest live news data



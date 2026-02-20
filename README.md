#  AI-Based News Summarization & Evaluation Web Application

## Project Overview

This project is an AI-powered web application that fetches real-time news articles and generates concise abstractive summaries using Transformer-based NLP models. It also evaluates the generated summaries using BLEU and ROUGE metrics to help users quickly understand news content.

---

##  Features

* Real-time news fetching using NewsAPI
* Abstractive text summarization using Transformer models (BART)
* Summary evaluation using BLEU and ROUGE metrics
* Category-based and keyword-based news search
* Pagination and dark mode support
* User-friendly and responsive interface

---

##  Technologies Used

* Python
* Flask
* Hugging Face Transformers (BART)
* NLTK (BLEU)
* ROUGE Score
* HTML, CSS, Jinja2
* NewsAPI

---


---

##  How to Run the Project

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Add your NewsAPI key in `app.py`

3. Run the Flask app:

```bash
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000/
```

---

## Output Preview

### Home Page (News Categories)

<img width="738" height="318" alt="image" src="https://github.com/user-attachments/assets/13a9a19c-50a7-41f3-afcc-fa92e63fc689" />

###  Search Functionality Output
<img width="738" height="355" alt="image" src="https://github.com/user-attachments/assets/573da5fa-b2fe-43b1-befc-2946894e5380" />

### Categories
<img width="737" height="347" alt="image" src="https://github.com/user-attachments/assets/c6d7aa4b-fba3-4aff-9024-4fdd3a45efca" />

##  Project Highlights

* Real-time NLP application using live news data
* End-to-end pipeline: data collection → summarization → evaluation → display
* Integrated evaluation metrics rarely seen in student projects
* Strong combination of NLP and web development

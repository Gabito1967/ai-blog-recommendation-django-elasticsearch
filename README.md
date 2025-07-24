# 🧠 AI Blog Recommendation System using Django + Elasticsearch + HuggingFace

A full-featured blog application built with Django, enhanced by AI-powered content recommendation using `sentence-transformers` + `FAISS`, and Elasticsearch-based smart search with fuzzy, autocomplete, synonym, and multi-language capabilities.

---

## 🚀 Features

- 🔍 **AI Post Recommendations** using Sentence Transformers + FAISS
- 🔎 **Full-Text Search** with Elasticsearch 8.x
- ⚡ Ultra-fast FAISS vector similarity search
- 🧠 SentenceTransformer: `all-MiniLM-L6-v2`
- 🧵 Clean Django Template frontend
- 📦 Easily pluggable into any blog or content system
- 📝 Create and manage blog posts with CKEditor 5.
- 📚 Categorized blog content.
- 🔍 Elasticsearch 8.13 integrated for:
  - Autocomplete suggestions
  - Fuzzy matching
  - Synonym handling
  - Multilingual indexing (e.g., Hindi, English)
  - Real-time search
- 🤖 AI-powered blog recommendations using:
  - HuggingFace Sentence Transformers
  - FAISS for fast vector similarity
- 📈 Blog analytics tracking (optional)
- 🌐 SEO-ready Django templates (no React/DRF frontend)

---

## 🛠 Tech Stack

- Python 3.10+
- Django 4.2
- Elasticsearch 8.x
- FAISS (Facebook AI Similarity Search)
- SentenceTransformers
- SQLite or PostgreSQL
- Bootstrap 5 (optional for UI)

---

## 🧠 AI Recommendation System

- Utilizes `sentence-transformers` for semantic embeddings.
- FAISS index built at runtime for similarity search.
- Suggests 5 most similar posts on the blog detail page based on title + intro content.

---

## 🔍 Elasticsearch Features

- Instant fuzzy search with highlight support.
- Synonym token filtering for related terms.
- Multi-language blog search support (English + Hindi).
- Live indexing of posts via Django signals (`post_save`).
- Search analytics (coming soon).




from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from .models import Post

model = SentenceTransformer('all-MiniLM-L6-v2')

# def get_ai_recommendations(post):
#     posts = Post.objects.exclude(id=post.id)
#     if not posts.exists():
#         return []

#     post_embedding = model.encode([post.title + " " + post.content[:100]])
#     all_embeddings = model.encode([p.title + " " + p.content[:100] for p in posts])

#     faiss_index = faiss.IndexFlatL2(384)
#     faiss_index.add(np.array(all_embeddings))

#     D, I = faiss_index.search(np.array(post_embedding), k=5)

#     similar_posts = [posts[int(i)] for i in I[0] if int(i) < len(posts)]

#     return similar_posts

def get_ai_recommendations(post):
    posts = Post.objects.exclude(id=post.id)
    if not posts.exists():
        return []

    post_embedding = model.encode([post.title + " " + post.content[:100]])
    all_embeddings = model.encode([p.title + " " + p.content[:100] for p in posts])

    faiss_index = faiss.IndexFlatL2(384)
    faiss_index.add(np.array(all_embeddings))

    D, I = faiss_index.search(np.array(post_embedding), k=5)

    similar_posts = [
        posts[int(i)]
        for i in I[0]
        if int(i) >= 0 and int(i) < len(posts)
    ]

    return similar_posts


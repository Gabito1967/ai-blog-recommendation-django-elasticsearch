from elasticsearch import Elasticsearch, exceptions as es_exceptions
from .models import Post

# Connect to Elasticsearch (ensure it's running)
es = Elasticsearch("http://localhost:9200")

def search_posts(query):
    if not query:
        return Post.objects.none()

    try:
        response = es.search(index="blog_posts", body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title^3", "content"],  # Boost title more
                    "fuzziness": "auto"
                }
            }
        })

        ids = [int(hit["_id"]) for hit in response["hits"]["hits"]]
        return Post.objects.filter(id__in=ids)

    except es_exceptions.ConnectionError as e:
        print("[x] Elasticsearch connection error:", e)
        return Post.objects.none()

    except Exception as e:
        print("[x] Search error:", e)
        return Post.objects.none()



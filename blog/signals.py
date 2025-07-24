from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def index_post(post):
    doc = {
        "title": post.title,
        "content": post.content,
    }
    es.index(index="blog_posts", id=post.id, body=doc)

def delete_post_from_index(post_id):
    es.delete(index="blog_posts", id=post_id, ignore=[404])

@receiver(post_save, sender=Post)
def post_saved(sender, instance, **kwargs):
    index_post(instance)

@receiver(post_delete, sender=Post)
def post_deleted(sender, instance, **kwargs):
    delete_post_from_index(instance.id)


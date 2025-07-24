from django.core.management.base import BaseCommand
from blog.models import Post
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

class Command(BaseCommand):
    help = 'Indexes all blog posts into Elasticsearch'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        for post in posts:
            doc = {
                "title": post.title,
                "content": post.content,
            }
            es.index(index="blog_posts", id=post.id, body=doc)
            self.stdout.write(self.style.SUCCESS(f"Indexed: {post.title}"))

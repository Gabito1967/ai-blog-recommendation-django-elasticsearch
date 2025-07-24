from django.shortcuts import render, get_object_or_404
from .models import Post
from .search import search_posts
from .recommendation import get_ai_recommendations

def post_list(request):
    posts = Post.objects.select_related('category').filter(status=1)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    ai_recommendations = get_ai_recommendations(post)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'recommendations': ai_recommendations
    })


def post_search(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        try:
            results = search_posts(query)
        except Exception as e:
            print(f"[x] Search error: {e}")
            results = []

    context = {
        'query': query,
        'results': results,
        'result_count': len(results),
    }
    return render(request, 'blog/search_results.html', context)


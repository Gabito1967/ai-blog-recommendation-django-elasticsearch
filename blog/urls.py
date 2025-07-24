from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail'),
    path('search/', views.post_search, name='post-search'),
]

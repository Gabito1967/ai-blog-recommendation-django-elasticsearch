from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['status', 'created_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_filter = ['status', 'category', 'created_at']

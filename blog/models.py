from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import escape
from django.urls import reverse
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('post-list-by-category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

   
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=240,unique=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d/', null=True, blank=True)
    content = CKEditor5Field(config_name='extends',blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Auto-generate slug from title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
  

    def __str__(self):
        return self.title  
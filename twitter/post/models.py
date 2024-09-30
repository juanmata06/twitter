from django.db import models
from django.db.models import SET_NULL
from user.models import User
from category.models import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
      return self.title

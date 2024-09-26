from django.contrib import admin
from post.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Primary information', {'fields': ('title', 'content', 'slug')}),
        ('More information', {'fields': ('miniature', 'is_visible', 'user', 'category')}),
    )
    list_display = ['title', 'is_visible', 'created_at']

from django.contrib import admin
from category.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Primary information', {'fields': ('title', 'slug', 'is_visible')}),
    )
    list_display = ['title', 'is_visible']
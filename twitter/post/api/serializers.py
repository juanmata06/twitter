from rest_framework import serializers
from post.models import Post
from user.api.serializers import UserGetSerializer
from category.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserGetSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug',
            'content', 'miniature', 'created_at',
            'is_visible', 'user', 'category'
        ]

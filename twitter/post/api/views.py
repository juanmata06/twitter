from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from post.models import Post
from post.api.serializers import PostSerializer
from post.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['-created_at']
    # filterset_fields = ['is_visible']
    filterset_fields = ['category__slug']
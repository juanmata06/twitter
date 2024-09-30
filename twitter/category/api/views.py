from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from category.models import Category
from category.api.serializers import CategorySerializer
from category.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # queryset = Category.objects.filter(is_visible=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['-slug']
    filterset_fields = ['is_visible', 'title']

from rest_framework.viewsets import ModelViewSet
from category.models import Category
from category.api.serializers import CategorySerializer

class CategoryApiViewSet(ModelViewSet):
  serializer_class = CategorySerializer  
  queryset = Category.objects.all()
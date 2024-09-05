from rest_framework.routers import DefaultRouter
from category.api.views import CategoryApiViewSet

router = DefaultRouter()
router.register(prefix='categories', viewset=CategoryApiViewSet)
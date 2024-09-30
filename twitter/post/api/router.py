from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet

router = DefaultRouter()
router.register(prefix='posts', viewset=PostApiViewSet)
"""
URL configuration for twitter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# General imports:
from django.contrib import admin
from django.urls import path, include
# Drfyasg config imports:
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# API views imports:
from category.api.router import router as category_router

schema_view = get_schema_view(
   openapi.Info(
      title="Twitter API",
      default_version='v1',
      description="It is a very basic example of the Twitter API, including users, permissions, posts, and comments.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="juanmataguzzo17@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('user.api.router')),
    path('api/', include(category_router.urls))
]

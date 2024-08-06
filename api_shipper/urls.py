from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PackageViewSet

router = DefaultRouter()
router.register(r'packages', PackageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
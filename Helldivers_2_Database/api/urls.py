from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FactionVIewSet

router = DefaultRouter()
router.register(r'factions', FactionVIewSet)

urlpatterns = [
    path('', include(router.urls)),
]

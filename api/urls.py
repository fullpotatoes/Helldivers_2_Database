from django.urls import path
from .views import factionsList

urlpatterns = [
    path('factions/', factionsList.as_view(), name='factions-list'),
]

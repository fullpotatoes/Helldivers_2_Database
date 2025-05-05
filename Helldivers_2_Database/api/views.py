from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Faction  # Updated import
from .serializers import FactionSerializer

class FactionVIewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer

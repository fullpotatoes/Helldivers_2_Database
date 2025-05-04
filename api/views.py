from rest_framework import generics
from api.models import factions
from api.serializers import factions_Serializer


class factionsList(generics.ListCreateAPIView):
    queryset = factions.objects.all()
    serializer_class = factions_Serializer

from rest_framework import serializers
from .models import factions

class factions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = factions
        fields = ["id", "name"]
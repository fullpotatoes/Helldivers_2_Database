from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Faction, Sector, Biome, Environmental, Planet,
    WeaponType, FireMode, WeaponTrait, Weapon,
    ArmorSlot, ArmorPassive, Armor, Booster, Item
)
from .serializers import (
    FactionSerializer, SectorSerializer, BiomeSerializer, EnvironmentalSerializer, PlanetSerializer,
    WeaponTypeSerializer, FireModeSerializer, WeaponTraitSerializer, WeaponSerializer,
    ArmorSlotSerializer, ArmorPassiveSerializer, ArmorSerializer, BoosterSerializer, ItemSerializer
)

def hello_world(request):
    # Create a context dictionary with data to pass to the template
    context = {
        'title': 'Hello Helldivers',
        'message': 'Welcome to the Helldivers 2 Database!',
        'items': ['Liberty', 'Democracy', 'Freedom'],
    }
    return render(request, 'planets.html', context)

def planet_list(request):
    planets = Planet.objects.all()
    context = {
        'title': 'Planets',
        'message': 'List of all planets in the Helldivers 2 universe',
        'planets': planets
    }
    return render(request, 'planets.html', context)

class FactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer

class SectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class BiomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Biome.objects.all()
    serializer_class = BiomeSerializer

class EnvironmentalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Environmental.objects.all()
    serializer_class = EnvironmentalSerializer

class PlanetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class WeaponTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeaponType.objects.all()
    serializer_class = WeaponTypeSerializer

class FireModeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FireMode.objects.all()
    serializer_class = FireModeSerializer

class WeaponTraitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeaponTrait.objects.all()
    serializer_class = WeaponTraitSerializer

class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class ArmorSlotViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArmorSlot.objects.all()
    serializer_class = ArmorSlotSerializer

class ArmorPassiveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArmorPassive.objects.all()
    serializer_class = ArmorPassiveSerializer

class ArmorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer

class BoosterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Booster.objects.all()
    serializer_class = BoosterSerializer

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

from rest_framework import serializers
from .models import (
    Faction, Sector, Biome, Environmental, Planet,
    WeaponType, FireMode, WeaponTrait, Weapon,
    ArmorSlot, ArmorPassive, Armor, Booster, Item
)

class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = ['id', 'name']

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'name']

class BiomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biome
        fields = ['id', 'name', 'description']

class EnvironmentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environmental
        fields = ['id', 'name', 'description']

class PlanetSerializer(serializers.ModelSerializer):
    sector = SectorSerializer(read_only=True)
    biome = BiomeSerializer(read_only=True)
    environmentals = EnvironmentalSerializer(many=True, read_only=True)

    class Meta:
        model = Planet
        fields = [
            'id', 'name', 'sector', 'biome', 'environmentals',
            'name_en_US', 'name_en_GB', 'name_pt_BR', 'name_de_DE',
            'name_es_ES', 'name_fr_FR', 'name_it_IT', 'name_ja_JP',
            'name_ko_KO', 'name_ms_MY', 'name_pl_PL'
        ]

class WeaponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponType
        fields = ['id', 'name']

class FireModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireMode
        fields = ['id', 'name']

class WeaponTraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponTrait
        fields = ['id', 'name', 'description']

class WeaponSerializer(serializers.ModelSerializer):
    type = WeaponTypeSerializer(read_only=True)
    fire_modes = FireModeSerializer(many=True, read_only=True)
    traits = WeaponTraitSerializer(many=True, read_only=True)

    class Meta:
        model = Weapon
        fields = [
            'id', 'name', 'description', 'type', 'damage', 'capacity',
            'recoil', 'fire_rate', 'fire_modes', 'traits',
            'is_primary', 'is_secondary', 'is_grenade'
        ]

class ArmorSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmorSlot
        fields = ['id', 'name']

class ArmorPassiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmorPassive
        fields = ['id', 'name', 'description']

class ArmorSerializer(serializers.ModelSerializer):
    slot = ArmorSlotSerializer(read_only=True)
    passive = ArmorPassiveSerializer(read_only=True)

    class Meta:
        model = Armor
        fields = [
            'id', 'name', 'description', 'type', 'slot',
            'armor_rating', 'speed', 'stamina_regen', 'passive'
        ]

class BoosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booster
        fields = ['id', 'name', 'description']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']

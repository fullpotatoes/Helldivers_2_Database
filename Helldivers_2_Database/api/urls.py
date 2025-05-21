from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FactionViewSet, SectorViewSet, BiomeViewSet, EnvironmentalViewSet, PlanetViewSet,
    WeaponTypeViewSet, FireModeViewSet, WeaponTraitViewSet, WeaponViewSet,
    ArmorSlotViewSet, ArmorPassiveViewSet, ArmorViewSet, BoosterViewSet, ItemViewSet, hello_world, planet_list
)

router = DefaultRouter()
router.register(r'factions', FactionViewSet)
router.register(r'sectors', SectorViewSet)
router.register(r'biomes', BiomeViewSet)
router.register(r'environmentals', EnvironmentalViewSet)
router.register(r'planets', PlanetViewSet)
router.register(r'weapon-types', WeaponTypeViewSet)
router.register(r'fire-modes', FireModeViewSet)
router.register(r'weapon-traits', WeaponTraitViewSet)
router.register(r'weapons', WeaponViewSet)
router.register(r'armor-slots', ArmorSlotViewSet)
router.register(r'armor-passives', ArmorPassiveViewSet)
router.register(r'armors', ArmorViewSet)
router.register(r'boosters', BoosterViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('planets/', planet_list, name='planets_list'),
    path('', include(router.urls)),
    path('admin/', include(router.urls))
]

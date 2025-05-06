from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import (
    Faction, Sector, Biome, Environmental, Planet,
    WeaponType, FireMode, WeaponTrait, Weapon,
    ArmorSlot, ArmorPassive, Armor, Booster, Item
)

class FactionAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faction1 = Faction.objects.create(name="Super Earth")
        self.faction2 = Faction.objects.create(name="Terminids")
        self.faction3 = Faction.objects.create(name="Automatons")

    def test_get_all_factions(self):
        """Test retrieving all factions"""
        url = reverse('faction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_single_faction(self):
        """Test retrieving a single faction"""
        url = reverse('faction-detail', args=[self.faction1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Super Earth')

class SectorAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sector1 = Sector.objects.create(name="Galactic Core")
        self.sector2 = Sector.objects.create(name="Outer Rim")

    def test_get_all_sectors(self):
        """Test retrieving all sectors"""
        url = reverse('sector-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_sector(self):
        """Test retrieving a single sector"""
        url = reverse('sector-detail', args=[self.sector1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Galactic Core')

class BiomeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.biome1 = Biome.objects.create(id="desert", name="Desert", description="Hot and dry")
        self.biome2 = Biome.objects.create(id="snow", name="Snow", description="Cold and icy")

    def test_get_all_biomes(self):
        """Test retrieving all biomes"""
        url = reverse('biome-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_biome(self):
        """Test retrieving a single biome"""
        url = reverse('biome-detail', args=[self.biome1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Desert')

class EnvironmentalAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.env1 = Environmental.objects.create(id="sandstorm", name="Sandstorm", description="Reduces visibility")
        self.env2 = Environmental.objects.create(id="blizzard", name="Blizzard", description="Reduces movement speed")

    def test_get_all_environmentals(self):
        """Test retrieving all environmentals"""
        url = reverse('environmental-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_environmental(self):
        """Test retrieving a single environmental"""
        url = reverse('environmental-detail', args=[self.env1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Sandstorm')

class PlanetAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sector = Sector.objects.create(name="Galactic Core")
        self.biome = Biome.objects.create(id="desert", name="Desert", description="Hot and dry")
        self.planet = Planet.objects.create(name="Arrakis", sector=self.sector, biome=self.biome)
        self.env = Environmental.objects.create(id="sandstorm", name="Sandstorm", description="Reduces visibility")
        self.planet.environmentals.add(self.env)

    def test_get_all_planets(self):
        """Test retrieving all planets"""
        url = reverse('planet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_planet(self):
        """Test retrieving a single planet"""
        url = reverse('planet-detail', args=[self.planet.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Arrakis')
        self.assertEqual(response.data['sector']['name'], 'Galactic Core')
        self.assertEqual(response.data['biome']['name'], 'Desert')
        self.assertEqual(response.data['environmentals'][0]['name'], 'Sandstorm')

class WeaponTypeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.type1 = WeaponType.objects.create(name="Assault Rifle")
        self.type2 = WeaponType.objects.create(name="Shotgun")

    def test_get_all_weapon_types(self):
        """Test retrieving all weapon types"""
        url = reverse('weapontype-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_weapon_type(self):
        """Test retrieving a single weapon type"""
        url = reverse('weapontype-detail', args=[self.type1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Assault Rifle')

class FireModeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.mode1 = FireMode.objects.create(name="Single")
        self.mode2 = FireMode.objects.create(name="Burst")

    def test_get_all_fire_modes(self):
        """Test retrieving all fire modes"""
        url = reverse('firemode-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_fire_mode(self):
        """Test retrieving a single fire mode"""
        url = reverse('firemode-detail', args=[self.mode1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Single')

class WeaponTraitAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.trait1 = WeaponTrait.objects.create(name="High Damage", description="Deals extra damage")
        self.trait2 = WeaponTrait.objects.create(name="Rapid Fire", description="Fires quickly")

    def test_get_all_weapon_traits(self):
        """Test retrieving all weapon traits"""
        url = reverse('weapontrait-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_weapon_trait(self):
        """Test retrieving a single weapon trait"""
        url = reverse('weapontrait-detail', args=[self.trait1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'High Damage')

class WeaponAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.type = WeaponType.objects.create(name="Assault Rifle")
        self.mode = FireMode.objects.create(name="Single")
        self.trait = WeaponTrait.objects.create(name="High Damage", description="Deals extra damage")
        self.weapon = Weapon.objects.create(
            id="ar1", name="AR-23 Liberator", description="Standard issue", 
            type=self.type, damage=50, capacity=30, recoil=20, fire_rate=600,
            is_primary=True
        )
        self.weapon.fire_modes.add(self.mode)
        self.weapon.traits.add(self.trait)

    def test_get_all_weapons(self):
        """Test retrieving all weapons"""
        url = reverse('weapon-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_weapon(self):
        """Test retrieving a single weapon"""
        url = reverse('weapon-detail', args=[self.weapon.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'AR-23 Liberator')
        self.assertEqual(response.data['type']['name'], 'Assault Rifle')
        self.assertEqual(response.data['fire_modes'][0]['name'], 'Single')
        self.assertEqual(response.data['traits'][0]['name'], 'High Damage')

class ArmorSlotAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.slot1 = ArmorSlot.objects.create(name="Helmet")
        self.slot2 = ArmorSlot.objects.create(name="Chest")

    def test_get_all_armor_slots(self):
        """Test retrieving all armor slots"""
        url = reverse('armorslot-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_armor_slot(self):
        """Test retrieving a single armor slot"""
        url = reverse('armorslot-detail', args=[self.slot1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Helmet')

class ArmorPassiveAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.passive1 = ArmorPassive.objects.create(name="Damage Reduction", description="Reduces incoming damage")
        self.passive2 = ArmorPassive.objects.create(name="Speed Boost", description="Increases movement speed")

    def test_get_all_armor_passives(self):
        """Test retrieving all armor passives"""
        url = reverse('armorpassive-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_armor_passive(self):
        """Test retrieving a single armor passive"""
        url = reverse('armorpassive-detail', args=[self.passive1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Damage Reduction')

class ArmorAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.slot = ArmorSlot.objects.create(name="Helmet")
        self.passive = ArmorPassive.objects.create(name="Damage Reduction", description="Reduces incoming damage")
        self.armor = Armor.objects.create(
            id="helm1", name="Combat Helmet", description="Standard issue", 
            type=1, slot=self.slot, armor_rating=50, speed=100, stamina_regen=100,
            passive=self.passive
        )

    def test_get_all_armors(self):
        """Test retrieving all armors"""
        url = reverse('armor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_armor(self):
        """Test retrieving a single armor"""
        url = reverse('armor-detail', args=[self.armor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Combat Helmet')
        self.assertEqual(response.data['slot']['name'], 'Helmet')
        self.assertEqual(response.data['passive']['name'], 'Damage Reduction')

class BoosterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booster1 = Booster.objects.create(id="boost1", name="Energy Drink", description="Increases stamina")
        self.booster2 = Booster.objects.create(id="boost2", name="Stim Pack", description="Increases health regen")

    def test_get_all_boosters(self):
        """Test retrieving all boosters"""
        url = reverse('booster-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_booster(self):
        """Test retrieving a single booster"""
        url = reverse('booster-detail', args=[self.booster1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Energy Drink')

class ItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Item.objects.create(id="item1", name="Medkit")
        self.item2 = Item.objects.create(id="item2", name="Ammo Pack")

    def test_get_all_items(self):
        """Test retrieving all items"""
        url = reverse('item-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_item(self):
        """Test retrieving a single item"""
        url = reverse('item-detail', args=[self.item1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Medkit')

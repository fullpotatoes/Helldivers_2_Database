from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Faction

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

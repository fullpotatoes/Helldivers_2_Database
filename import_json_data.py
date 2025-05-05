import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Helldivers_2_Database.settings')
django.setup()

from Helldivers_2_Database.api.models import factions

def import_factions():
    print("importing factions data...")
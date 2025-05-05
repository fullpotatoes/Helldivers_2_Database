import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Helldivers_2_Database.settings')
django.setup()

from Helldivers_2_Database.api.models import Faction

def import_factions():
    print("importing factions data...")

    json_file_path = 'Helldivers_2_Database/Json_ressources/Json/factions.json'

    try:

        with open(json_file_path, 'r') as file:
            factions_data = json.load(file)

        for faction_id, faction_name in factions_data.items():
            faction, created = Faction.objects.update_or_create(
                id=int(faction_id),
                defaults={'name': faction_name}
            )

            if created:
                print(f"Created faction: {faction_name}")
            else:
                print(f"Updated faction: {faction_name}")

        print("Factions import completed successfully!")

    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing factions {e}")

if __name__ == "__main__":
    import_factions()

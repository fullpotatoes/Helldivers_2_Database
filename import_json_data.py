import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Helldivers_2_Database.settings')
django.setup()

from Helldivers_2_Database.api.models import (
    Faction, Sector, Biome, Environmental, Planet, 
    WeaponType, FireMode, WeaponTrait, Weapon,
    ArmorSlot, ArmorPassive, Armor, Booster, Item
)

def import_factions():
    print("Importing factions data...")
    json_file_path = 'Ressources/Json/factions.json'
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
        print(f"Error importing factions: {e}")

def import_biomes():
    print("Importing biomes data...")
    json_file_path = 'Ressources/Json/planets/biomes.json'
    try:
        with open(json_file_path, 'r') as file:
            biomes_data = json.load(file)
        for biome_id, biome_info in biomes_data.items():
            biome, created = Biome.objects.update_or_create(
                id=biome_id,
                defaults={
                    'name': biome_info['name'],
                    'description': biome_info['description']
                }
            )
            if created:
                print(f"Created biome: {biome.name}")
            else:
                print(f"Updated biome: {biome.name}")
        print("Biomes import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing biomes: {e}")

def import_environmentals():
    print("Importing environmentals data...")
    json_file_path = 'Ressources/Json/planets/environmentals.json'
    try:
        with open(json_file_path, 'r') as file:
            environmentals_data = json.load(file)
        for env_id, env_info in environmentals_data.items():
            env, created = Environmental.objects.update_or_create(
                id=env_id,
                defaults={
                    'name': env_info['name'],
                    'description': env_info['description']
                }
            )
            if created:
                print(f"Created environmental: {env.name}")
            else:
                print(f"Updated environmental: {env.name}")
        print("Environmentals import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing environmentals: {e}")

def import_planets():
    print("Importing planets data...")
    json_file_path = 'Ressources/Json/planets/planets.json'
    try:
        with open(json_file_path, 'r') as file:
            planets_data = json.load(file)

        for planet_id, planet_info in planets_data.items():
            # Get or create sector
            sector_name = planet_info.get('sector', 'Unknown')
            sector, _ = Sector.objects.get_or_create(name=sector_name)

            # Get biome (if exists)
            biome = None
            biome_id = planet_info.get('biome')
            if biome_id:
                try:
                    biome = Biome.objects.get(id=biome_id)
                except Biome.DoesNotExist:
                    print(f"Warning: Biome {biome_id} not found for planet {planet_info['name']}")

            # Create planet
            planet_data = {
                'name': planet_info['name'],
                'sector': sector,
                'biome': biome,
            }

            # Add localized names if available
            if 'names' in planet_info:
                names = planet_info['names']
                for lang, name in names.items():
                    lang_field = f'name_{lang.replace("-", "_")}'
                    if hasattr(Planet, lang_field):
                        planet_data[lang_field] = name

            planet, created = Planet.objects.update_or_create(
                id=int(planet_id),
                defaults=planet_data
            )

            # Add environmentals
            if 'environmentals' in planet_info:
                planet.environmentals.clear()
                for env_id in planet_info['environmentals']:
                    try:
                        env = Environmental.objects.get(id=env_id)
                        planet.environmentals.add(env)
                    except Environmental.DoesNotExist:
                        print(f"Warning: Environmental {env_id} not found for planet {planet.name}")

            if created:
                print(f"Created planet: {planet.name}")
            else:
                print(f"Updated planet: {planet.name}")

        print("Planets import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing planets: {e}")

def import_weapon_types():
    print("Importing weapon types data...")
    json_file_path = 'Ressources/Json/items/weapons/types.json'
    try:
        with open(json_file_path, 'r') as file:
            types_data = json.load(file)
        for type_id, type_name in types_data.items():
            weapon_type, created = WeaponType.objects.update_or_create(
                id=int(type_id),
                defaults={'name': type_name}
            )
            if created:
                print(f"Created weapon type: {type_name}")
            else:
                print(f"Updated weapon type: {type_name}")
        print("Weapon types import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing weapon types: {e}")

def import_fire_modes():
    print("Importing fire modes data...")
    json_file_path = 'Ressources/Json/items/weapons/fire_modes.json'
    try:
        with open(json_file_path, 'r') as file:
            modes_data = json.load(file)
        for mode_id, mode_name in modes_data.items():
            fire_mode, created = FireMode.objects.update_or_create(
                id=int(mode_id),
                defaults={'name': mode_name}
            )
            if created:
                print(f"Created fire mode: {mode_name}")
            else:
                print(f"Updated fire mode: {mode_name}")
        print("Fire modes import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing fire modes: {e}")

def import_weapon_traits():
    print("Importing weapon traits data...")
    json_file_path = 'Ressources/Json/items/weapons/traits.json'
    try:
        with open(json_file_path, 'r') as file:
            traits_data = json.load(file)
        for trait_id, trait_info in traits_data.items():
            trait, created = WeaponTrait.objects.update_or_create(
                id=int(trait_id),
                defaults={
                    'name': trait_info['name'],
                    'description': trait_info.get('description', '')
                }
            )
            if created:
                print(f"Created weapon trait: {trait.name}")
            else:
                print(f"Updated weapon trait: {trait.name}")
        print("Weapon traits import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing weapon traits: {e}")

def import_weapons(file_path, is_primary=False, is_secondary=False, is_grenade=False):
    print(f"Importing weapons from {file_path}...")
    try:
        with open(file_path, 'r') as file:
            weapons_data = json.load(file)

        for weapon_id, weapon_info in weapons_data.items():
            # Get weapon type if exists
            weapon_type = None
            if 'type' in weapon_info:
                try:
                    weapon_type = WeaponType.objects.get(id=weapon_info['type'])
                except WeaponType.DoesNotExist:
                    print(f"Warning: Weapon type {weapon_info['type']} not found for weapon {weapon_info['name']}")

            # Create weapon
            weapon_data = {
                'name': weapon_info['name'],
                'description': weapon_info.get('description', ''),
                'type': weapon_type,
                'damage': weapon_info.get('damage', 0),
                'capacity': weapon_info.get('capacity', 0),
                'recoil': weapon_info.get('recoil', 0),
                'fire_rate': weapon_info.get('fire_rate', 0),
                'is_primary': is_primary,
                'is_secondary': is_secondary,
                'is_grenade': is_grenade,
            }

            weapon, created = Weapon.objects.update_or_create(
                id=weapon_id,
                defaults=weapon_data
            )

            # Add fire modes
            if 'fire_mode' in weapon_info:
                weapon.fire_modes.clear()
                for mode_id in weapon_info['fire_mode']:
                    try:
                        mode = FireMode.objects.get(id=mode_id)
                        weapon.fire_modes.add(mode)
                    except FireMode.DoesNotExist:
                        print(f"Warning: Fire mode {mode_id} not found for weapon {weapon.name}")

            # Add traits
            if 'traits' in weapon_info:
                weapon.traits.clear()
                for trait_id in weapon_info['traits']:
                    try:
                        trait = WeaponTrait.objects.get(id=trait_id)
                        weapon.traits.add(trait)
                    except WeaponTrait.DoesNotExist:
                        print(f"Warning: Trait {trait_id} not found for weapon {weapon.name}")

            if created:
                print(f"Created weapon: {weapon.name}")
            else:
                print(f"Updated weapon: {weapon.name}")

        print(f"Weapons import from {file_path} completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {file_path}")
    except Exception as e:
        print(f"Error importing weapons from {file_path}: {e}")

def import_all_weapons():
    import_weapon_types()
    import_fire_modes()
    import_weapon_traits()

    # Import primary weapons
    import_weapons('Ressources/Json/items/weapons/primary.json', is_primary=True)

    # Import secondary weapons
    import_weapons('Ressources/Json/items/weapons/secondary.json', is_secondary=True)

    # Import grenades
    import_weapons('Ressources/Json/items/weapons/grenades.json', is_grenade=True)

def import_armor_slots():
    print("Importing armor slots data...")
    json_file_path = 'Ressources/Json/items/armor/slot.json'
    try:
        with open(json_file_path, 'r') as file:
            slots_data = json.load(file)
        for slot_id, slot_name in slots_data.items():
            slot, created = ArmorSlot.objects.update_or_create(
                id=int(slot_id),
                defaults={'name': slot_name}
            )
            if created:
                print(f"Created armor slot: {slot_name}")
            else:
                print(f"Updated armor slot: {slot_name}")
        print("Armor slots import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing armor slots: {e}")

def import_armor_passives():
    print("Importing armor passives data...")
    json_file_path = 'Ressources/Json/items/armor/passive.json'
    try:
        with open(json_file_path, 'r') as file:
            passives_data = json.load(file)
        for passive_id, passive_info in passives_data.items():
            passive, created = ArmorPassive.objects.update_or_create(
                id=int(passive_id),
                defaults={
                    'name': passive_info['name'],
                    'description': passive_info.get('description', '')
                }
            )
            if created:
                print(f"Created armor passive: {passive.name}")
            else:
                print(f"Updated armor passive: {passive.name}")
        print("Armor passives import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing armor passives: {e}")

def import_armors():
    print("Importing armors data...")
    json_file_path = 'Ressources/Json/items/armor/armor.json'
    try:
        with open(json_file_path, 'r') as file:
            armors_data = json.load(file)

        for armor_id, armor_info in armors_data.items():
            # Get armor slot if exists
            armor_slot = None
            if 'slot' in armor_info:
                try:
                    armor_slot = ArmorSlot.objects.get(id=armor_info['slot'])
                except ArmorSlot.DoesNotExist:
                    print(f"Warning: Armor slot {armor_info['slot']} not found for armor {armor_info['name']}")

            # Get armor passive if exists
            armor_passive = None
            if 'passive' in armor_info and armor_info['passive'] != 0:
                try:
                    armor_passive = ArmorPassive.objects.get(id=armor_info['passive'])
                except ArmorPassive.DoesNotExist:
                    print(f"Warning: Armor passive {armor_info['passive']} not found for armor {armor_info['name']}")

            # Create armor
            armor_data = {
                'name': armor_info['name'],
                'description': armor_info.get('description', ''),
                'type': armor_info.get('type', 0),
                'slot': armor_slot,
                'armor_rating': armor_info.get('armor_rating', 100),
                'speed': armor_info.get('speed', 100),
                'stamina_regen': armor_info.get('stamina_regen', 100),
                'passive': armor_passive,
            }

            armor, created = Armor.objects.update_or_create(
                id=armor_id,
                defaults=armor_data
            )

            if created:
                print(f"Created armor: {armor.name}")
            else:
                print(f"Updated armor: {armor.name}")

        print("Armors import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing armors: {e}")

def import_all_armors():
    import_armor_slots()
    import_armor_passives()
    import_armors()

def import_boosters():
    print("Importing boosters data...")
    json_file_path = 'Ressources/Json/items/boosters.json'
    try:
        with open(json_file_path, 'r') as file:
            boosters_data = json.load(file)

        for booster_id, booster_info in boosters_data.items():
            booster, created = Booster.objects.update_or_create(
                id=booster_id,
                defaults={
                    'name': booster_info['name'],
                    'description': booster_info.get('description', '')
                }
            )

            if created:
                print(f"Created booster: {booster.name}")
            else:
                print(f"Updated booster: {booster.name}")

        print("Boosters import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing boosters: {e}")

def import_items():
    print("Importing items data...")
    json_file_path = 'Ressources/Json/items/item_names.json'
    try:
        with open(json_file_path, 'r') as file:
            items_data = json.load(file)

        for item_id, item_info in items_data.items():
            item, created = Item.objects.update_or_create(
                id=item_id,
                defaults={
                    'name': item_info['name']
                }
            )

            if created:
                print(f"Created item: {item.name}")
            else:
                print(f"Updated item: {item.name}")

        print("Items import completed successfully!")
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {json_file_path}")
    except Exception as e:
        print(f"Error importing items: {e}")

def import_all_data():
    import_factions()
    import_biomes()
    import_environmentals()
    import_planets()
    import_all_weapons()
    import_all_armors()
    import_boosters()
    import_items()
    print("All data imported successfully!")

if __name__ == "__main__":
    import_all_data()

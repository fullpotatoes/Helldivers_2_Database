from django.db import models

class Faction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Faction"
        verbose_name_plural = "Factions"
        db_table = "factions"

    def __str__(self):
        return self.name

class Sector(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"
        db_table = "sectors"

    def __str__(self):
        return self.name

class Biome(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Using the key from JSON as ID
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Biome"
        verbose_name_plural = "Biomes"
        db_table = "biomes"

    def __str__(self):
        return self.name

class Environmental(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Using the key from JSON as ID
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Environmental"
        verbose_name_plural = "Environmentals"
        db_table = "environmentals"

    def __str__(self):
        return self.name

class Planet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='planets')
    biome = models.ForeignKey(Biome, on_delete=models.SET_NULL, null=True, related_name='planets')
    environmentals = models.ManyToManyField(Environmental, related_name='planets')

    # For localized names
    name_en_US = models.CharField(max_length=200, blank=True, null=True)
    name_en_GB = models.CharField(max_length=200, blank=True, null=True)
    name_pt_BR = models.CharField(max_length=200, blank=True, null=True)
    name_de_DE = models.CharField(max_length=200, blank=True, null=True)
    name_es_ES = models.CharField(max_length=200, blank=True, null=True)
    name_fr_FR = models.CharField(max_length=200, blank=True, null=True)
    name_it_IT = models.CharField(max_length=200, blank=True, null=True)
    name_ja_JP = models.CharField(max_length=200, blank=True, null=True)
    name_ko_KO = models.CharField(max_length=200, blank=True, null=True)
    name_ms_MY = models.CharField(max_length=200, blank=True, null=True)
    name_pl_PL = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Planet"
        verbose_name_plural = "Planets"
        db_table = "planets"

    def __str__(self):
        return self.name

# Weapon-related models
class WeaponType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Weapon Type"
        verbose_name_plural = "Weapon Types"
        db_table = "weapon_types"

    def __str__(self):
        return self.name

class FireMode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Fire Mode"
        verbose_name_plural = "Fire Modes"
        db_table = "fire_modes"

    def __str__(self):
        return self.name

class WeaponTrait(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Weapon Trait"
        verbose_name_plural = "Weapon Traits"
        db_table = "weapon_traits"

    def __str__(self):
        return self.name

class Weapon(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Using mix_id from JSON
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(WeaponType, on_delete=models.SET_NULL, null=True, related_name='weapons')
    damage = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    recoil = models.IntegerField(default=0)
    fire_rate = models.IntegerField(default=0)
    fire_modes = models.ManyToManyField(FireMode, related_name='weapons')
    traits = models.ManyToManyField(WeaponTrait, related_name='weapons')
    is_primary = models.BooleanField(default=False)
    is_secondary = models.BooleanField(default=False)
    is_grenade = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Weapon"
        verbose_name_plural = "Weapons"
        db_table = "weapons"

    def __str__(self):
        return self.name

# Armor-related models
class ArmorSlot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Armor Slot"
        verbose_name_plural = "Armor Slots"
        db_table = "armor_slots"

    def __str__(self):
        return self.name

class ArmorPassive(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Armor Passive"
        verbose_name_plural = "Armor Passives"
        db_table = "armor_passives"

    def __str__(self):
        return self.name

class Armor(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Using ID from JSON
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    type = models.IntegerField(default=0)
    slot = models.ForeignKey(ArmorSlot, on_delete=models.SET_NULL, null=True, related_name='armors')
    armor_rating = models.IntegerField(default=100)
    speed = models.IntegerField(default=100)
    stamina_regen = models.IntegerField(default=100)
    passive = models.ForeignKey(ArmorPassive, on_delete=models.SET_NULL, null=True, related_name='armors')

    class Meta:
        verbose_name = "Armor"
        verbose_name_plural = "Armors"
        db_table = "armors"

    def __str__(self):
        return self.name

class Booster(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Using ID from JSON
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Booster"
        verbose_name_plural = "Boosters"
        db_table = "boosters"

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Using mix_id from JSON
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        db_table = "items"

    def __str__(self):
        return self.name

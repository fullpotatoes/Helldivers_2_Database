# Generated by Django 4.2 on 2025-05-05 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='factions',
            new_name='Faction',
        ),
        migrations.AlterModelOptions(
            name='faction',
            options={'verbose_name': 'Faction', 'verbose_name_plural': 'Factions'},
        ),
        migrations.AlterModelTable(
            name='faction',
            table='factions',
        ),
    ]

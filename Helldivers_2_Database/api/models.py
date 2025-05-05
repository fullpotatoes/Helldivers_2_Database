from django.db import models

class factions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Faction"
        verbose_name_plural = "Factions"
        db_table = "factions"

    def __str__(self):
        return self.name
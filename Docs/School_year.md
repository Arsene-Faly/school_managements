--Créer view année scolaire

| id | name      | start_date | end_date   | is_active || Actions                              |
| -: | --------- | ---------- | ---------- | --------- || Voir - Modifier - Supprimer - Switch |
|  1 | 2025-2026 | 2025-09-01 | 2026-06-30 | False     || Voir - Modifier - Supprimer - Switch |
|  2 | 2026-2027 | 2026-09-01 | 2027-06-30 | True      || Voir - Modifier - Supprimer - Switch |
|  3 | 2027-2028 | 2027-09-01 | 2028-06-30 | False     || Voir - Modifier - Supprimer - Switch |


## Models

```py
from django.db import models

class SchoolYear(models.Model):
    name = models.CharField(max_length=9)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Année scolaire"
        verbose_name_plural = "Années scolaires"

    def __str__(self):
        return self.name
```

## Donée Seed

```py

from datetime import date

from django.core.management.base import BaseCommand
from schools.models import SchoolYear

class Command(BaseCommand):
    help = "Générer les années scolaires de 2026 à 2035"

    def handle(self, *args, **options):
        # Une seule année scolaire active
        SchoolYear.objects.update(is_active=False)

        for year in range(2026, 2036):
            name = f"{year}-{year + 1}"

            school_year, created = SchoolYear.objects.update_or_create(
                name=name,
                defaults={
                    "start_date": date(year, 9, 1),
                    "end_date": date(year + 1, 6, 30),
                    "is_active": year == 2026,
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Créée : {school_year}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Mise à jour : {school_year}")
                )

        self.stdout.write(
            self.style.SUCCESS("Génération terminée avec succès !")
        )
```
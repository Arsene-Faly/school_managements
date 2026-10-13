
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

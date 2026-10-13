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

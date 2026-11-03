from schools.models import SchoolYear


def validate_school_year(name, start_date, end_date, exclude_id=None):

    errors = {}

    # Validation du nom
    if not name:
        errors["name"] = "Le nom est obligatoire."

    else:
        school_years = SchoolYear.objects.filter(name__iexact=name)

        # Exclure l'année actuelle pendant la modification
        if exclude_id:
            school_years = school_years.exclude(id=exclude_id)

        if school_years.exists():
            errors["name"] = "Cette année scolaire existe déjà."

    # Validation date début
    if not start_date:
        errors["start_date"] = "La date de début est obligatoire."

    # Validation date fin
    if not end_date:
        errors["end_date"] = "La date de fin est obligatoire."

    elif start_date and end_date <= start_date:
        errors["end_date"] = (
            "La date de fin doit être supérieure à la date de début."
        )

    return errors
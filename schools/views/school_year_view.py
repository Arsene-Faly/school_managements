from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from schools.models import SchoolYear
from django.views.decorators.http import require_POST

def school_year_view(request):
    school_years = SchoolYear.objects.all()
    
    context = {
        "pages": "school_year",
        "school_years": school_years,
    }

    return render(request, "pages/admin/school_year/list.html", context)

@require_POST
def school_year_switch_view(request, id):
    school_year = get_object_or_404(SchoolYear, id=id)

    with transaction.atomic():
        if school_year.is_active:
            # Empêcher de désactiver l'année active
            # sans en activer une autre
            pass
        else:
            SchoolYear.objects.update(is_active=False)
            school_year.is_active = True
            school_year.save(update_fields=["is_active"])

    return redirect("school_year")
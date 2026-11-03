from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from schools.models import SchoolYear
from django.views.decorators.http import require_POST
from schools.validators.school_year_validator import validate_school_year
from django.contrib import messages

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

def school_year_detail_view(request, id):
    school_year = get_object_or_404(SchoolYear, id=id)

    context = {
        "pages": "school_year",
        "school_year": school_year,
    }

    return render(request, "pages/admin/school_year/detail.html", context)

def school_year_create_view(request):

    errors = {}
    form_data = {}

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        form_data = {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
        }

        errors = validate_school_year(
            name,
            start_date,
            end_date
        )

        if not errors:
            SchoolYear.objects.create(
                name=name,
                start_date=start_date,
                end_date=end_date,
            )

            return redirect("school_year")

    context = {
        "pages": "school_year",
        "errors": errors,
        "form_data": form_data,
    }

    return render(
        request,
        "pages/admin/school_year/create.html",
        context
    )
    
def school_year_edit_view(request, id):

    school_year = get_object_or_404(SchoolYear, id=id)

    errors = {}

    form_data = {
        "name": school_year.name,
        "start_date": school_year.start_date,
        "end_date": school_year.end_date,
    }

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        form_data = {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
        }

        errors = validate_school_year(
            name,
            start_date,
            end_date,
            exclude_id=school_year.id
        )

        if not errors:
            school_year.name = name
            school_year.start_date = start_date
            school_year.end_date = end_date

            school_year.save()

            return redirect("school_year")

    context = {
        "pages": "school_year",
        "school_year": school_year,
        "errors": errors,
        "form_data": form_data,
    }

    return render(
        request,
        "pages/admin/school_year/edit.html",
        context
    )
    
@require_POST
def school_year_delete_view(request, id):

    school_year = get_object_or_404(SchoolYear, id=id)

    if school_year.is_active:
        messages.error(
            request,
            "Impossible de supprimer l'année scolaire active."
        )
    else:
        school_year.delete()

        messages.success(
            request,
            "Année scolaire supprimée avec succès."
        )

    return redirect("school_year")
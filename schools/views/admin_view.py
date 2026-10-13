from django.shortcuts import render

def dashboard_view(request):
    context = {
        "pages" : "admin"
    }
    return render(request, "pages/admin/index.html", context)
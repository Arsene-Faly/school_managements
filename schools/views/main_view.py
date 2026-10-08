from django.shortcuts import render

def home_view(request):
    return render(request, "pages/index.html")

def about_view(request):
    return render(request, "pages/about.html")

def service_view(request):
    return render(request, "pages/service.html")
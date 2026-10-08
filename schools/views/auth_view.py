from django.shortcuts import render

def login_view(request):
    return render(request, "pages/auth/login.html")

def register_view(request):
    return render(request, "pages/auth/register.html")
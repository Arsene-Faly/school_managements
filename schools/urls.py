from django.urls import path
from schools.views.main_view import home_view, about_view, service_view
from schools.views.auth_view import login_view, register_view
from schools.views.admin_view import dashboard_view

urlpatterns = [
    # URL PAR DEFAUT
    path('', home_view, name='home'),
    path('service/', service_view, name='service'),
    path('about/', about_view, name='about'),
    
    # URL AUTHENTIFICATION
    path('auth/login/', login_view, name='login'),
    path('auth/register/', register_view, name='register'),
    
    # URL ADMIN
    path('admin_page/', dashboard_view, name='dashboard'),
]

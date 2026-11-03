from django.urls import path
from schools.views.main_view import home_view, about_view, service_view
from schools.views.auth_view import login_view, register_view
from schools.views.admin_view import dashboard_view
from schools.views.school_year_view import *

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
    
    # Année Scolaire
    path('admin_page/année_scolaire', school_year_view, name='school_year'),
    path("admin_page/school-years/<int:id>/switch/", school_year_switch_view, name="school_year_switch",),
    path("school-years/<int:id>/", school_year_detail_view, name="school_year_detail"),
    path("school-years/create/", school_year_create_view, name="school_year_create"),
    path("school-years/<int:id>/edit/", school_year_edit_view, name="school_year_edit"),
    path("school-years/<int:id>/delete/", school_year_delete_view, name="school_year_delete"),
]

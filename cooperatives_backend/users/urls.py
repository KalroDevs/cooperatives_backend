from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SaccoRegistry

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login_view, name='login'),    
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout_confirm.html', next_page='login'), name='logout'),
    path('redirect/', views.role_redirect, name='role_redirect'),
    path('register/', views.register_view, name='register'),  # registration   
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboards/', views.dashboards, name='dashboards'),
    path('staff_dashboard/', views.national_dashboard, name='national_dashboard'),
    path('county_dashboard/', views.county_dashboard, name='county_dashboard'),
    path('fa_dashboard/', views.fa_dashboard, name='fa_dashboard'),
    path('sp_dashboard/', views.sp_dashboard, name='sp_dashboard'),


    path('sacco_registry/', SaccoRegistry.as_view(), name='sacco_registry'),

    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]

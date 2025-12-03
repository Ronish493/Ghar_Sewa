from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'), 
    path('', include('users.urls')),
    path('dashboard/', include('dashboard.urls')), 


    path('', lambda r: redirect('index'), name='index'),
    path('about/', lambda r: render(r, 'about.html'), name='about'),
    path('services/', lambda r: render(r, 'service.html'), name='service'),
    path('team/', lambda r: render(r, 'team.html'), name='team'),
    path('testimonial/', lambda r: render(r, 'testimonial.html'), name='testimonial'),
    path('contact/', lambda r: render(r, 'contact.html'), name='contact'),
]
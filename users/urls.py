from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact_view, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('painting/', views.painting, name='painting'),
    path('plastering/', views.plastering, name='plastering'),
    path('electrical/', views.electrical, name='electrical'),
    path('plumbing/', views.plumbing, name='plumbing'),
    path('carpentry/', views.carpentry, name='carpentry'),
    path('flooring/', views.flooring, name='flooring'),
    path('roofing/', views.roofing, name='roofing'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('appliance/', views.appliance, name='appliance'),
    path('services/', include('allservices.urls')),

]

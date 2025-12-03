from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('profile/', views.profile, name='user_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('update_booking_status/', views.update_booking_status, name='update_booking_status'),
    path('service-bookings/', views.service_bookings, name='service_bookings'),
    path('service-bookings/view/<int:booking_id>/', views.view_booking, name='view_booking'),
    path('service-bookings/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('service-bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('service-bookings/add/', views.add_booking, name='add_booking'),
    path('service-providers/', views.service_providers, name='service_providers'),
    path('service-providers/add/', views.add_service_provider, name='add_service_provider'),
    path('service-providers/edit/<int:provider_id>/', views.edit_service_provider, name='edit_provider'),
    path('service-providers/delete/<int:provider_id>/', views.delete_service_provider, name='delete_provider'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('update_profile_photo/', views.update_profile_photo, name='update_profile_photo'),  # Add this line
    path('manage_users/', views.manage_users, name='manage_users'),
    path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('change_user_password/<int:user_id>/', views.change_user_password, name='change_user_password'),
]
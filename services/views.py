from django.shortcuts import render, redirect
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})


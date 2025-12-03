from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import authenticate
from .forms import LoginForm 
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.auth.backends import ModelBackend


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'users/home.html')

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Make sure 'home' is the correct URL name
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'registration/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Explicitly specify the backend when logging in
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        else:
            messages.error(request, 'Error in signup process')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        # User confirmed logout, perform logout and redirect
        logout(request)
        return redirect('index')  # Redirect to the index page after logging out
    
    # If GET request, show the confirmation page
    return render(request, 'registration/logout.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            full_message = f"Message from {name} <{email}>:\n\n{message}"

            send_mail(
                subject,
                full_message,
                email,
                ['researchofficial55@gmail.com'],  # receiver
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def appointment(request):
    return render(request, 'appointment.html')

def feature(request):
    return render(request, 'feature.html')

def contact(request):
    return render(request, 'contact.html')

def painting(request):
    return render(request, 'service/painting.html')

def plastering(request):
    return render(request, 'service/plastering.html')

def electrical(request):
    return render(request, 'service/electrical.html')

def plumbing(request):
    return render(request, 'service/plumbing.html')

def carpentry(request):
    return render(request, 'service/carpentry.html')

def flooring(request): 
    return render(request, 'service/flooring.html')

def roofing(request):
    return render(request, 'service/roofing.html')

def cleaning(request):
    return render(request, 'service/cleaning.html')

def appliance(request):
    return render(request, 'service/appliance.html')








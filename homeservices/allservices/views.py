from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ServiceBooking
from .forms import ServiceBookingForm

# Mapping service types to templates (small improvement: uppercase constant name)
SERVICE_TEMPLATES = {
    'appliance': 'service/appliance.html',
    'cleaning': 'service/cleaning.html',
    'electrical': 'service/electrical.html',
    'flooring': 'service/flooring.html',
    'painting': 'service/painting.html',
    'plastering': 'service/plastering.html',
    'plumbing': 'service/plumbing.html',
    'roofing': 'service/roofing.html',
}

def get_service_template(service_type):
    """Return the template path for a given service type."""
    return SERVICE_TEMPLATES.get(service_type)


@login_required(login_url='/login/')
def service_list(request):
    """Display the list of services."""
    return render(request, 'service/service.html')


@login_required(login_url='/login/')
def book_service(request, service_type):
    """Handle booking logic for all service types."""
    
    template_path = get_service_template(service_type)

    # Invalid service type
    if not template_path:
        messages.error(request, "Invalid service type.")
        return redirect('service')

    if request.method == 'POST':
        form = ServiceBookingForm(request.POST, service_type=service_type)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # attach logged-in user
            booking.save()
            messages.success(request, "Service booked successfully!")
            return redirect('booking_success')
        else:
            # Debug print (kept small improvement)
            print("Form errors:", form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        # GET request — load empty form
        form = ServiceBookingForm(service_type=service_type)

    return render(request, template_path, {
        'form': form,
        'service_type': service_type
    })


@login_required(login_url='/login/')
def booking_success(request):
    """Simple success page after booking."""
    return render(request, 'service/booking_success.html')

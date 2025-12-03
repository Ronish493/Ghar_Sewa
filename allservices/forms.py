from django import forms
from .models import ServiceBooking, ServiceProvider

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ['name', 'email', 'phone', 'address', 'preferred_date', 'note']  # Removed 'service'
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        self.service_type = kwargs.pop('service_type', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.service = self.service_type  # Set service from URL parameter
        if commit:
            instance.save()
        return instance
    
class AdminServiceBookingForm(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ['name', 'email', 'phone', 'address', 'service', 'preferred_date', 'note', 'revenue']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 4}),
            'service': forms.Select(choices=ServiceBooking.SERVICE_TYPES),
        }

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name', 'email', 'phone', 'address', 'age', 'service_type', 'photo', 'is_active']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),
            'service_type': forms.Select(choices=ServiceProvider.SERVICE_TYPES),
        }
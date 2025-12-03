from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=True, label="Full Name")
    email = forms.EmailField(max_length=254, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Split the name into first and last names
        name_parts = self.cleaned_data['name'].split()
        if len(name_parts) > 1:
            user.first_name = name_parts[0]
            user.last_name = ' '.join(name_parts[1:])
        else:
            user.first_name = name_parts[0]
            user.last_name = ''
        user.name = self.cleaned_data['name']
        
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    login = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
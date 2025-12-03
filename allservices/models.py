from django.db import models

class ServiceBooking(models.Model):
    SERVICE_TYPES = (
        ('cleaning', 'Cleaning'),
        ('painting', 'Painting'),
        ('roofing', 'Roofing'),
        ('electrical', 'Electrical'),
        ('flooring', 'Flooring'),
        ('plastering', 'Plastering'),
        ('plumbing', 'Plumbing'),
        ('appliance', 'Appliance'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    service = models.CharField(max_length=100, choices=SERVICE_TYPES)
    preferred_date = models.DateField()
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.service} - #{self.id}"
    

class ServiceProvider(models.Model):
    SERVICE_TYPES = (
        ('cleaning', 'Cleaning'),
        ('painting', 'Painting'),
        ('roofing', 'Roofing'),
        ('electrical', 'Electrical'),
        ('flooring', 'Flooring'),
        ('plastering', 'Plastering'),
        ('plumbing', 'Plumbing'),
        ('appliance', 'Appliance'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    age = models.PositiveIntegerField()
    service_type = models.CharField(max_length=100, choices=SERVICE_TYPES)
    photo = models.ImageField(upload_to='provider_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
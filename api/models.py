from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)  # e.g., Dog, Cat
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    is_adopted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pets/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Adopter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username


class AdoptionApplication(models.Model):
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.adopter.user.username} - {self.pet.name}"


class Veterinarian(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    clinic_address = models.TextField()
    available_times = models.TextField()  # Example: "Monday-Friday: 10am-6pm"

    def __str__(self):
        return self.name


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default="Admin")

    def __str__(self):
        return self.user.username


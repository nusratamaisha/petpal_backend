from django.contrib import admin
from .models import Pet, Adopter, Veterinarian, AdoptionApplication, Admin

admin.site.register(Pet)
admin.site.register(Adopter)
admin.site.register(Veterinarian)
admin.site.register(AdoptionApplication)
admin.site.register(Admin)

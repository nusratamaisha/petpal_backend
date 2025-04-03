from rest_framework import serializers
from .models import Pet, AdoptionApplication, Veterinarian, Adopter, Admin

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class AdopterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopter
        fields = '__all__'

class AdoptionApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionApplication
        fields = '__all__'

class VeterinarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinarian
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

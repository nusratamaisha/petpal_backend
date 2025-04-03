from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.AllowAny]
    
    
class AdopterViewSet(viewsets.ModelViewSet):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class AdoptionApplicationViewSet(viewsets.ModelViewSet):
    queryset = AdoptionApplication.objects.all()
    serializer_class = AdoptionApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class VeterinarianViewSet(viewsets.ModelViewSet):
    queryset = Veterinarian.objects.all()
    serializer_class = VeterinarianSerializer
    permission_classes = [permissions.AllowAny]
    
    
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAdminUser]


@api_view(['GET'])
def api_list(request):
    api_urls = {
        'Pets': '/pets/',
        'Adopters': '/adopters/',
        'Veterinarians': '/veterinarians/',
        'Adoption Applications': '/adoption_applications/',
        'Admin': '/admins',
    }
    return Response(api_urls)
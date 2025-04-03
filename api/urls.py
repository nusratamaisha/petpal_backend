from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'pets', PetViewSet, basename='pets')
router.register(r'adopters', AdopterViewSet, basename='adopters')
router.register(r'adoption_applications', AdoptionApplicationViewSet, basename='adoption_applications')
router.register(r'veterinarians', VeterinarianViewSet, basename='veterinarians')
router.register(r'admins', AdminViewSet, basename='admins')


urlpatterns = [
    path('', include(router.urls)), 
    path('api-list/', api_list, name='api-list'),
]

from django.urls import path, include
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register(r'year', viewsets.YearViewSet, basename='year')
router.register(r'all', viewsets.PNPViewSet, basename='all')
router.register(r'institution', viewsets.InstitutionViewSet, basename='institution')


urlpatterns = [
    path('', include(router.urls)),
]
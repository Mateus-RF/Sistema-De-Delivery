from django.shortcuts import render

# Create your views here.

# Task 7
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class RestauranteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.filter(tipo='restaurante')
    serializer_class = UsuarioSerializer
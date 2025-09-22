from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Usuário (Cliente ou Restaurante) - Task 7 
class Usuario(AbstractUser):
    TIPOS = (
        ('cliente', 'Cliente'),
        ('restaurante', 'Restaurante'),
    )
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)

    REQUIRED_FIELDS = ['email', 'nome', 'tipo']

    def __str__(self):
        return self.nome
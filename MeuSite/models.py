from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    fornecedor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('fornecedor', 'Fornecedor'),
        ('comprador', 'Comprador'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

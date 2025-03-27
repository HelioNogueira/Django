from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_fornecedor = models.BooleanField(default=False)

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    fornecedor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

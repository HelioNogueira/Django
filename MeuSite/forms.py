from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Produto

class CustomUserForm(UserCreationForm):
    """Formulário para criação de usuários personalizados."""
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class ProdutoForm(forms.ModelForm):
    """Formulário para cadastrar produtos."""
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade']

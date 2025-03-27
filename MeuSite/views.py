from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required

# Tela de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:  # Vendedor
                return redirect('home_venda')
            else:  # Comprador
                return redirect('home_compra')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Página do vendedor (Cadastro de produtos)
@login_required
def home_venda_view(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_venda')
    else:
        form = ProdutoForm()
    produtos = Produto.objects.all()
    return render(request, 'home_venda.html', {'form': form, 'produtos': produtos})

# Página do comprador (Visualizar produtos)
def home_compra_view(request):
    produtos = Produto.objects.all()
    return render(request, 'home_compra.html', {'produtos': produtos})

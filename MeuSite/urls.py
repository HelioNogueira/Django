from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('compra/', views.home_compra_view, name='home_compra'),
    path('venda/', views.home_venda_view, name='home_venda'),
    path('logout/', views.logout_view, name='logout'),
]

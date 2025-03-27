from django.contrib import admin
from django.urls import path, include
from MeuSite import urls as MeuSite_urls

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include(MeuSite_urls))
]

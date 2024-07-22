"""
URL configuration for Proyecto_Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from App_Final import views

urlpatterns = [
    path('', views.inicio),
    path('login/', views.login),
    path('registro/', views.registro),
    path('detalle/<id_producto>', views.detalle),
    path('perfil/<id_usuario>', views.perfil),
    path('pruebaInsertar/<nombre>/<numero>', views.curso)
]

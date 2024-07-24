# from App_Final.models import Curso
from django.http import HttpResponse
from django.template import loader

# def curso(request, nombre, numero):
#     curso = Curso(nombre=nombre, camada=int(numero))
#     curso.save()
#     documento = f"Curso: {curso.nombre}<br>Camada: {curso.camada}"
#     return HttpResponse(documento)

def inicio(request):
    productos = {"cosmeticos": ["Base", "Corrector", "Rubor", "Labial"]}

    plantilla = loader.get_template('App_Final/index.html')

    documento = plantilla.render(productos)

    return HttpResponse(documento)

def login(request):
    plantilla = loader.get_template('App_Final/login.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def registro(request):
    plantilla = loader.get_template('App_Final/registro.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def perfil(request, id_usuario):
    plantilla = loader.get_template('App_Final/perfil.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def productos(request):
    plantilla = loader.get_template('App_Final/productos.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def detalle(request, id_producto):
    plantilla = loader.get_template('App_Final/detalle.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def articulos(request):
    plantilla = loader.get_template('App_Final/articulos.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def ver_mas(request, id_producto):
    plantilla = loader.get_template('App_Final/ver_mas.html')

    documento = plantilla.render()

    return HttpResponse(documento)
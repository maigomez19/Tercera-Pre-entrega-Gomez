from App_Final.models import Producto, Usuario, Articulo
from django.http import HttpResponse
from django.template import loader
from App_Final.forms import ProductoFormulario, UsuarioFormulario, ArticuloFormulario
from django.shortcuts import render

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
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            producto = Producto(nombre=informacion["nombre"], detalle=informacion["detalle"], precio=informacion["precio"], seccion_rostro=informacion["seccion_rostro"])
            producto.save()

            return render(request, "App_Final/productos.html")
    else:
        formulario = ProductoFormulario()

    return render(request, "App_Final/productos.html", {"formulario": formulario})

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
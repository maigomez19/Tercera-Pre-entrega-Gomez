from App_Final.models import Producto, Usuario, Articulo
from django.http import HttpResponse
from django.template import loader
from App_Final.forms import ProductoFormulario, UsuarioFormulario, ArticuloFormulario
from django.shortcuts import render
from datetime import date

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
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = Usuario(
                nombre=informacion["nombre"], 
                apellido=informacion["apellido"], 
                email=informacion["email"],
                clave=hash(informacion["clave"]), 
                rol=2,
            )
            usuario.save()

            formulario = UsuarioFormulario()

            return render(request, "App_Final/registro.html", {"formulario": formulario})
    else:
        formulario = UsuarioFormulario()

    return render(request, "App_Final/registro.html", {"formulario": formulario})

def perfil(request, id_usuario):
    plantilla = loader.get_template('App_Final/perfil.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def productos(request):
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            producto = Producto(
                nombre=informacion["nombre"], 
                detalle=informacion["detalle"], 
                precio=informacion["precio"], 
                seccion_rostro=informacion["seccion_rostro"]
            )
            producto.save()

            formulario = ProductoFormulario()

            return render(request, "App_Final/productos.html", {"formulario": formulario})
    else:
        formulario = ProductoFormulario()

    return render(request, "App_Final/productos.html", {"formulario": formulario})

def detalle(request, id_producto):
    plantilla = loader.get_template('App_Final/detalle.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def articulos(request):
    if request.method == 'POST':
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            articulo = Articulo(
                titulo=informacion["titulo"], 
                detalle=informacion["detalle"],
                fecha=date.today, 
                autor=informacion["autor"], 
                clasificacion=informacion["clasificacion"]
            )
            articulo.save()

            formulario = ArticuloFormulario()

            return render(request, "App_Final/articulos.html", {"formulario": formulario})
    else:
        formulario = ArticuloFormulario()

    return render(request, "App_Final/articulos.html", {"formulario": formulario})
    

def ver_mas(request, id_producto):
    plantilla = loader.get_template('App_Final/ver_mas.html')

    documento = plantilla.render()

    return HttpResponse(documento)
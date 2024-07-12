from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Inicio")

def login(request):
    return HttpResponse("Login")

def registro(request):
    return HttpResponse("Registro")

def detalle(request, id_producto):
    return HttpResponse(f"Detalle producto ID: {id_producto}")

def perfil(request, id_usuario):
    return HttpResponse(f"Perfil usuario ID: {id_usuario}")
from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    inicio_html = open('./Proyecto_Final/plantillas/index.html')

    plantilla = Template(inicio_html.read())

    inicio_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def login(request):
    login_html = open('./Proyecto_Final/plantillas/login.html')

    plantilla = Template(login_html.read())

    login_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def registro(request):
    registro_html = open('./Proyecto_Final/plantillas/registro.html')

    plantilla = Template(registro_html.read())

    registro_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def detalle(request, id_producto):
    detalle_html = open('./Proyecto_Final/plantillas/detalle.html')

    plantilla = Template(detalle_html.read())

    detalle_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def perfil(request, id_usuario):
    perfil_html = open('./Proyecto_Final/plantillas/perfil.html')

    plantilla = Template(perfil_html.read())

    perfil_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
from django import forms

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    detalle = forms.CharField()
    precio = forms.DecimalField(max_digits=6,decimal_places=2)
    seccion_rostro = forms.CharField(max_length=40)

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    clave = forms.CharField(max_length=20)
    rol = forms.IntegerField()

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    detalle = forms.CharField()
    autor = forms.CharField(max_length=40)
    clasificacion = forms.CharField(max_length=40)
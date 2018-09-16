from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response 
from appSoyEco.models import Usuario
from rest_framework import generics
from appSoyEco.serializers import UsuarioSerializer
 
""" def principal(request): 
     return render_to_response("principal.html")
def principal(request): 
    usuarios = Usuario.objects.all() 
    return render_to_response("principal.html", { 'usuarios':usuarios } ) """

def principal(request): 
    usuarios = Usuario.objects.all() 
    return render_to_response("principal.html", {"usuarios":usuarios})

def principalajax(request): 
    return render_to_response("principalajax.html")

class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
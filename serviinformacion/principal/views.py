from django.shortcuts import render

# Create your views here.
from rest_framework import serializer
from .models import AccesoControl, Departamentos, Municipio, MesaJurado, Perfiles, UsuariosVotos
from .serializer import AccesoControlSerialize,DepartamentosSerialize,MesajuradoSerialize,MunicipioSerialize,PerfilesSerialize

class AutoAPI(viewsets.ModelViewSet):
	#clase generica
	
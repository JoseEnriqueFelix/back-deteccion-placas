from django.shortcuts import render
from rest_framework import generics
from .models import Incidencia, Operador, Usuario, Vehiculo 
from .serializers import IncidenciaSerializer, OperadorSerializer, UsuarioSerializer, VehiculoSerializer


class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = "pk"

class VehiculoListCreate(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    
class VehiculoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    lookup_field = "pk"
    
class OperadorListCreate(generics.ListCreateAPIView):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer
    
class OperadorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer
    lookup_field = "pk"
    
class IncidenciaListCreate(generics.ListCreateAPIView):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer
    
class IncidenciaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer
    lookup_field = "pk"
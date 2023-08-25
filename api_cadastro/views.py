from django.shortcuts import render
from rest_framework import viewsets
from api_cadastro.serializers import *
from api_cadastro.models import *

# Create your views here.

class cad_instrutorViewset(viewsets.ModelViewSet):
    queryset = cad_instrutor.objects.all()
    serializer_class = cad_instrutorSerializer

class cad_salaViewset(viewsets.ModelViewSet):
    queryset = cad_sala.objects.all()
    serializer_class = cad_salaSerializer

class EventoViewset(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
class ImagemViewset(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
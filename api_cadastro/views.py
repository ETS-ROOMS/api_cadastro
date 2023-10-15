from rest_framework import viewsets
from api_cadastro.serializers import *
from api_cadastro.models import *
from rest_framework.response import Response

# Create your views here.

def extract_url(image_record):
    return image_record['Imagem']

class cad_instrutorViewset(viewsets.ModelViewSet):
    queryset = cad_instrutor.objects.all()
    serializer_class = cad_instrutorSerializer

class cad_salaViewset(viewsets.ModelViewSet):
    queryset = cad_sala.objects.all()
    serializer_class = cad_salaSerializer

    def list(self, request):
        queryset = cad_sala.objects.all()

        salas = {}

        for sala in queryset:
            key = str(sala.id_sala)
            salas[key] = cad_salaSerializer(sala).data
            imgs_queryset = Imagem.objects.filter(sala=sala)
            salas[key]['images'] = map(extract_url, ImagemSerializer(imgs_queryset, many=True).data)
            
        return Response(list(salas.values()))

class EventoViewset(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ImagemViewset(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
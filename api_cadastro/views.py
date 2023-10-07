from rest_framework import viewsets
from api_cadastro.serializers import *
from api_cadastro.models import *
from rest_framework.response import Response

# Create your views here.


class cad_instrutorViewset(viewsets.ModelViewSet):
    queryset = cad_instrutor.objects.all()
    serializer_class = cad_instrutorSerializer


class cad_salaViewset(viewsets.ModelViewSet):
    queryset = cad_sala.objects.all()
    serializer_class = cad_salaSerializer

    def list(self, request):
        queryset = cad_sala.objects.all()
        serializer = cad_salaSerializer(queryset, many=True)
        return Response(serializer.data)


class EventoViewset(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def list(self, request):
        day = request.query_params.get('day')
        queryset = Evento.objects.filter(data_inicio=day, data_fim=day)
        serializer = EventoSerializer(queryset, many=True)
        return Response(serializer.data)

class ImagemViewset(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

from rest_framework import viewsets
from api_cadastro.serializers import *
from api_cadastro.models import *
from rest_framework.response import Response

# Create your views here.

def extract_url(image_record):
    return image_record['Imagem']

class MateriaViewset(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


class InstrutorViewset(viewsets.ModelViewSet):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer

    def list(self, request):
        queryset = Instrutor.objects.all()

        instrutores = {}

        for instrutor in queryset:
            key = str(instrutor.id_instrutor)
            instrutores[key] = InstrutorSerializer(instrutor).data
            materias_qset = Materia.objects.filter(instrutor=instrutor)
            instrutores[key]['materias'] = MateriaSerializer(materias_qset, many=True).data
        
        return Response(list(instrutores.values()))

class SalaViewset(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    def list(self, request):
        queryset = Sala.objects.all()

        salas = {}

        for sala in queryset:
            key = str(sala.id_sala)
            salas[key] = SalaSerializer(sala).data
            imgs_queryset = Imagem.objects.filter(sala=sala)
            salas[key]['images'] = map(extract_url, ImagemSerializer(imgs_queryset, many=True).data)
            
        return Response(list(salas.values()))


class EventoViewset(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def list(self, request):
        day = request.query_params.get('day')
        if day == None:
            queryset = Evento.objects.all().order_by('-historico')
        else:
            queryset = Evento.objects.filter(data_inicio=day, data_fim=day)

        eventos = []

        for idx, evt in enumerate(queryset):
            data = EventoSerializer(evt).data
            data['instrutor_data'] = InstrutorSerializer(Instrutor.objects.get(pk=data['instrutor'])).data
            data['materia_data'] = MateriaSerializer(Materia.objects.get(pk=data['materia'])).data
            eventos.append(data)

        return Response(eventos)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except DateTakenError as e:
            return Response({"error": str(e)}, status=400)



class ImagemViewset(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

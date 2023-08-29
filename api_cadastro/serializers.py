from rest_framework import serializers
from api_cadastro.models import *


class cad_instrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = cad_instrutor
        fields = '__all__'

class cad_salaSerializer(serializers.ModelSerializer):
    class Meta:
        model= cad_sala
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'
        
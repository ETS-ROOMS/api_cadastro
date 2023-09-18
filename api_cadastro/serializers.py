from rest_framework import serializers
from api_cadastro.models import *


class cad_instrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = cad_instrutor
        fields = '__all__'

class cad_salaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cad_sala
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    # hora_inicio = serializers.SerializerMethodField()
    # data_inicio = serializers.SerializerMethodField()
    # historico = serializers.SerializerMethodField()

    class Meta:
        model = Evento
        fields = '__all__'


    #Aqui Estou pegando os campos "data_inicio, hora_inicio, historico" e formatando com a função "strftime"

    # def get_hora_inicio(self, obj):
    #     return obj.hora_inicio.strftime('%H:%M')
        
    # def get_data_inicio(self, obj):
    #     return obj.data_inicio.strftime('%m/%d')
    

    # def get_historico(self, obj): 
    #     return obj.historico.strftime('%m/%d ás %H:%M') 

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'

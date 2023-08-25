from django.db import models
from uuid import uuid4
from model_utils import FieldTracker

# CADASTRAR INSTRUTOR
class cad_instrutor(models.Model):
    id_instrutor = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100) 
    edv = models.CharField(max_length=8)
    email = models.CharField(max_length=150)
    cor = models.CharField(max_length=20)
    MATERIAS = (
        ('Fundamentos da Programação','Fundamentos da Programação'),
        ('Ingles', 'Ingles'),
        ('Office', 'Office'),
        ('Programação Orientada a Objeto', 'Programação Orientada a Objeto')
    )
    materias = models.CharField(max_length=200, choices=MATERIAS)

    def __str__(self):
        return "{} {}".format(self.nome, self.materias)
    
#CADASTRAR SALAS
class cad_sala(models.Model):
    id_sala = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_sala = models.CharField(max_length=20)
    PREDIO = (
        ('1', 'Ca600-ETS'),
        ('2', 'Ca170-ETS'),
        ('3', 'Ca140-ETS'),
    )
    predio_sala = models.CharField(max_length=1, choices=PREDIO, default=1)
    localizacao_sala = models.CharField(max_length=100)
    capacidade = models.IntegerField(default=0)
    computador = models.IntegerField(default=0)
    quadro_branco = models.IntegerField(default=0)
    projetor = models.IntegerField(default=0)
    televisao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_sala

#ARMAZERNAR IMAGENS DAS SALAS
class Imagem(models.Model):
    sala = models.ForeignKey(cad_sala, on_delete=models.CASCADE)
    Imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return f'Imagem da Sala {self.sala.nome_sala}'



#CRIAR EVENTOS
class Evento(models.Model):
    id_Evento = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_responsavel = models.ForeignKey(cad_instrutor, on_delete=models.CASCADE)
    nome_evento = models.CharField(max_length=100)
    edv_cliente = models.IntegerField()
    email = models.EmailField()
    descricao = models.CharField(max_length=500)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()



#------------------------------------------------------------------------------------------------------------#
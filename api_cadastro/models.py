from django.db import models
from django.core.exceptions import ValidationError
from uuid import uuid4

""" Campo de Informações do modelo

-Email removido a pedido da tay todos foram avisados 14/09/2023 **
-Criei o campo historico para registrar o momento em que foi solicitado 14/09/2023
-Criação do metodo clean e save no modelo Evento para evitar horarios conflitantes entre eventos 26/09/2023



"""


class cad_instrutor(models.Model):
    id_instrutor = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100) 
    edv = models.CharField(max_length=8)
    email = models.CharField(max_length=150)
    cor = models.CharField(max_length=20)
    materias = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.nome, self.cor)
    
class cad_sala(models.Model):
    id_sala = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_sala = models.CharField(max_length=20)
    PREDIO = (
        ('Ca600', 'Ca600'),
        ('Ca170', 'Ca170'),
        ('Ca140', 'Ca140'),
    )
    predio_sala = models.CharField(max_length=5, choices=PREDIO)
    localizacao_sala = models.CharField(max_length=100)
    capacidade = models.IntegerField(default=0)
    computador = models.IntegerField(default=0)
    quadro_branco = models.IntegerField(default=0)
    projetor = models.IntegerField(default=0)
    televisao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_sala, self.localizacao_sala
    
class Imagem(models.Model):
    sala = models.ForeignKey(cad_sala, on_delete=models.CASCADE)
    Imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return f'Imagem da Sala {self.sala.nome_sala}'


class Evento(models.Model):
    id_Evento = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_responsavel = models.CharField(max_length=250)
    nome_evento = models.CharField(max_length=100)
    edv_cliente = models.IntegerField()
    descricao = models.CharField(max_length=500)
    data_inicio = models.DateField()  
    data_fim = models.DateField()  
    hora_inicio = models.TimeField()  
    hora_fim = models.TimeField() 
    local = models.CharField(max_length=20)
    nome_sala = models.CharField(max_length=20)
    historico = models.DateTimeField(auto_now=True, editable=False)

#Metodo clean(Validações personalizada vos dados do modelo (antes de serem salvos))
    def clean(self):

        if self.hora_inicio == self.hora_fim:
            raise ValidationError("A hora de início não pode ser igual à hora de término.")

    #Verificando se á conflito no horario entre os eventos 
        eventos_conflitantes = Evento.objects.exclude(id_Evento=self.id_Evento).filter(
            data_fim=self.data_inicio,
            hora_fim__gte=self.hora_inicio,
            local=self.local,
            nome_sala=self.nome_sala
        )
        if eventos_conflitantes.exists():
            raise ValidationError("Existe um conflito de horário com outro evento no mesmo local e sala.")

        
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
   


#------------------------------------------------------------------------------------------------------------#

# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
from api_cadastro.models import Sala, Imagem, Instrutor
from django.core.files.images import ImageFile
from django.core.files import File

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete Sala instances")
    Sala.objects.all().delete()


def seed_db():
    print("Creating default salas")

    img_prefix = "seed_files"
    
    ca_600 = "Ca600"
    ca_170 = "Ca170"
    ca_140 = "Ca140"

    sala = Sala(
        nome_sala="Lab. DS 1",
        predio_sala=ca_600,
        localizacao_sala="Térreo",
        capacidade=19,
        computador=18,
        quadro_branco=0,
        projetor=0,
        televisao=1,
    )
    sala.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_DS1.1.jpg', "rb"), name="lab_DS1.1.jpg")
    )
    img.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_DS1.2.jpg', "rb"), name="lab_DS1.2.jpg")
    )
    img.save()
    print("{} sala created.".format(sala))

    sala = Sala(
        nome_sala="Lab. DS 2",
        predio_sala=ca_600,
        localizacao_sala="Térreo",
        capacidade=19,
        computador=18,
        quadro_branco=0,
        projetor=0,
        televisao=1,
    )
    sala.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_DS2.1.jpg', "rb"), name="lab_DS2.1.jpg")
    )
    img.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_DS2.2.jpg', "rb"), name="lab_DS2.2.jpg")
    )
    img.save()
    print("{} sala created.".format(sala))

    sala = Sala(
        nome_sala="Lab. DS 3",
        predio_sala=ca_600,
        localizacao_sala="Térreo",
        capacidade=25,
        computador=18,
        quadro_branco=0,
        projetor=0,
        televisao=1,
    )
    sala.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_DS3.1.jpg', "rb"), name="lab_DS3.1.jpg")
    )
    img.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_DS3.2.png', "rb"), name="lab_DS3.2.png")
    )
    img.save()
    print("{} sala created.".format(sala))

    sala = Sala(
        nome_sala="Lab. DS ETS",
        predio_sala=ca_170,
        localizacao_sala="Sub solo",
        capacidade=19,
        computador=18,
        quadro_branco=1,
        projetor=0,
        televisao=1,
    )
    sala.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_ets1.jpg', "rb"), name="lab_ets1.jpg")
    )
    img.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_ets2.jpg', "rb"), name="lab_ets2.jpg")
    )
    img.save()
    print("{} sala created.".format(sala))

    sala = Sala(
        nome_sala="Lab. Eletrônica",
        predio_sala=ca_170,
        localizacao_sala="Sub solo",
        capacidade=17,
        computador=16,
        quadro_branco=0,
        projetor=0,
        televisao=1,
    )
    sala.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_eletronica1.jpg', "rb"), name="lab_eletronica1.jpg")
    )
    img.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/lab_eletronica2.jpg', "rb"), name="lab_eletronica2.jpg")
    )
    img.save()
    print("{} sala created.".format(sala))
    
    sala = Sala(
        nome_sala="Sala de Reunião",
        predio_sala=ca_170,
        localizacao_sala="Sub solo",
        capacidade=8,
        computador=0,
        quadro_branco=0,
        projetor=0,
        televisao=1,
    )
    sala.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/sala_reuniao1.jpg', "rb"), name="sala_reuniao1.jpg")
    )
    img.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/sala_reuniao2.jpg', "rb"), name="sala_reuniao2.jpg")
    )
    img.save()
    print("{} sala created.".format(sala))

    sala = Sala(
        nome_sala="Sala Verde",
        predio_sala=ca_140,
        localizacao_sala="Sub solo",
        capacidade=19,
        computador=0,
        quadro_branco=1,
        projetor=4,
        televisao=1,
    )
    sala.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/sala_verde1.jpg', "rb"), name="sala_verde1.jpg")
    )
    img.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/sala_verde2.jpg', "rb"), name="sala_verde2.jpg")
    )
    img.save()
    print("{} sala created.".format(sala))

    sala = Sala(
        nome_sala="Sala Amarela",
        predio_sala=ca_140,
        localizacao_sala="Sub solo",
        capacidade=19,
        computador=0,
        quadro_branco=1,
        projetor=0,
        televisao=1,
    )
    sala.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/sala_amarela1.jpg', "rb"), name="sala_amarela1.jpg")
    )
    img.save()
    img = Imagem(
        sala=sala,
        Imagem=ImageFile(open(f'{img_prefix}/sala_amarela2.jpg', "rb"), name="sala_amarela2.jpg")
    )
    img.save()
    print("{} sala created.".format(sala))

    # -- Instrutores seed

    Instrutor(
        
    )
    

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    seed_db()
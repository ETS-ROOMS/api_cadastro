# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
from api_cadastro.models import cad_sala, Imagem
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
    cad_sala.objects.all().delete()


def seed_db():
    print("Creating default salas")

    img_prefix = "seed_files"
    
    ca_600 = "Ca600"

    sala = cad_sala(
        nome_sala="Sala 1",
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
        Imagem=ImageFile(open(f'{img_prefix}/lab_DS1.png', "rb"), name="lab_DS1.png")
    )
    img.save()
    print("{} sala created.".format(sala))
    return sala

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
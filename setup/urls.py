from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from api_cadastro.models import *
from api_cadastro.views import*
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('cad_instrutor', cad_instrutorViewset, basename='cad_instrutor')
router.register('cad_sala', cad_salaViewset, basename='cad_sala')
router.register('evento', EventoViewset, basename='evento')
router.register('imagens', ImagemViewset, basename='imagens')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.contrib import admin
from api_cadastro.models import cad_instrutor, cad_sala,Imagem

# Register your models here.

class ImagemInline(admin.TabularInline):
    model = Imagem

@admin.register(cad_sala)
class SalaAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]

admin.site.register(Imagem)
admin.site.register(cad_instrutor)
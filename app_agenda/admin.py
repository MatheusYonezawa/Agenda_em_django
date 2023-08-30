from django.contrib import admin
from app_agenda.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo' , 'data_evento', 'data_criacao', 'local_evento', 'descricao')
    list_filter = ('usuario', 'data_evento')

admin.site.register(Evento, EventoAdmin)
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Evento(models.Model):
    titulo= models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_evento = models.DateTimeField(verbose_name="Data do evento")
    data_criacao = models.DateTimeField(auto_now=True, verbose_name="Data de crianção")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local_evento = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'evento'

    def __str__(self) :
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')
    
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
    
    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
from django.db import models

class Evento (models.Model):
    titulo = models.TextField(max_length=100)
    descricao = models.TextField()
    data_evento = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    finalizado = models.BooleanField(default = False)
    
    def __str__ (self):
        return self.titulo


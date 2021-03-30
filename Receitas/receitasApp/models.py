from django.db import models
from datetime import datetime

# Create your models here.
class Receita(models.Model):        # Subclasse
    nome_receita = models.CharField(max_length=200)     # Campo para nome
    ingredientes = models.TextField()                   # Campo para texto grande
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receitas = models.DateTimeField(default=datetime.now, blank=True)

    # Terminal, mesma pasta de manage.py:
    ###     python manage.py makemigrations ###
    ###     python manage.py migrate ###
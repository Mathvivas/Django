from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=40)
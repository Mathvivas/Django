from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=40)

    # Substitui o nome padrão (Pessoa object(1)) para o nome da Pessoa
    def __str__(self):
        return self.nome
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):

    MASCULINO = 1
    FEMININO = 2
    SEXO = (
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
    )

    class Meta:

        db_table = 'cliente'

    nome = models.CharField(verbose_name = 'nome do cliente',max_length=100)
    idade = models.IntegerField(verbose_name='idade')
    sexo = models.IntegerField(choices=SEXO, default = '')
    formacao = models.CharField(verbose_name='Formação', max_length=100)


    def __str__(self):
        return self.nome
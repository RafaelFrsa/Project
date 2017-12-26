from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Resultado(models.Model):
	result_fl = models.CharField('Resultado FluidoDinamico', max_length=7000)	
	result_pres = models.CharField('Resultado Queda de Pressa', max_length=7000)
	result_geral = models.CharField('Resultado de Analise Geral', max_length=7000)		


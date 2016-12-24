from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Agua(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP', blank=True)
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k', blank=True)
	kt = models.BooleanField()

	class Meta:
		verbose_name='Agua'
		verbose_name_plural='Aguas'


class Butano(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k', blank=True)

class CO2(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class Metano(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class Pentano(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class RC318(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class Choice(models.Model):

	Agua = models.ForeignKey('Agua', blank=True, null=True)
	Butano = models.ForeignKey('Butano', blank=True, null=True)
	CO2 = models.ForeignKey('CO2', blank=True, null=True)
	Metano = models.ForeignKey('Metano', blank=True, null=True)	
	Pentano = models.ForeignKey('Pentano', blank=True, null=True)
	RC318 = models.ForeignKey('RC318', blank=True, null=True)



class Resultado(models.Model):
	result_dpl_tubo = models.CharField('Resultado Duplo Tubo:', max_length=7000)	


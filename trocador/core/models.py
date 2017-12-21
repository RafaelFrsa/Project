from django.db import models

# Create your models here.
class Fluido(models.Model):
    temperature = models.FloatField('Temperatura')
    pressure = models.FloatField('Pressao')
    Densidade= models.FloatField('Densidade')
    cp = models.FloatField('CP', blank=True)
    Viscos = models.FloatField('Viscosidade')
    k = models.FloatField('k', blank=True)

class Agua(Fluido):
    class Meta:
        verbose_name='Agua'

class Butano(Fluido):
    class Meta:
        verbose_name='Butano'

class Pentano(Fluido):
    class Meta:
        verbose_name='Pentano'

class RC318(Fluido):
    class Meta:
        verbose_name='RC318'

class CO2(Fluido):
    class Meta:
        verbose_name='CO2'

class Metano(Fluido):
    class Meta:
        verbose_name='Metano'
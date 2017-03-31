from django.contrib import admin

# Register your models here.
from trocador.cascoetubos.models import Agua, Butano, CO2, Metano, Pentano, RC318, Resultado

# Register your models here.
admin.site.register(Agua)
admin.site.register(Butano)
admin.site.register(CO2)
admin.site.register(Metano)
admin.site.register(Pentano)
admin.site.register(RC318)
admin.site.register(Resultado)
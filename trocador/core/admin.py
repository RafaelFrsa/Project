from django.contrib import admin

# Register your models here.
from trocador.core.models import Fluido, Agua, Butano, CO2, Metano, Pentano, RC318

# Register your models here.
admin.site.register(Fluido)
admin.site.register(Agua)
admin.site.register(Butano)
admin.site.register(CO2)
admin.site.register(Metano)
admin.site.register(Pentano)
admin.site.register(RC318)

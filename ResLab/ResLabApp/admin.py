from django.contrib import admin

from .models import Usuario
from .models import Departamento
from .models import Laboratorio
from .models import Software
from .models import Horario
from .models import Reserva

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Departamento)
admin.site.register(Laboratorio)
admin.site.register(Software)
admin.site.register(Horario)
admin.site.register(Reserva)

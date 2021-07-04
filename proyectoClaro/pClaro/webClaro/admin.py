from django.contrib import admin
from .models import Cliente, Comuna, ImagenPerfil, ServicioContratado, TecnologiaServicio
from .models import EstadoInstalacion, PlanContratado, CantidadDecodificadores 

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(ImagenPerfil)
admin.site.register(ServicioContratado)
admin.site.register(TecnologiaServicio)
admin.site.register(PlanContratado)
admin.site.register(CantidadDecodificadores)
admin.site.register(EstadoInstalacion)

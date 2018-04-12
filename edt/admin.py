from django.contrib import admin
from edt.models import *
# Register your models here.
### Admin

class EntryAdmin(admin.ModelAdmin):
    list_display = ["creator", "date", "title", "snippet"]
    list_filter = ["creator"]
    
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Permiso)
admin.site.register(Resolucion)
admin.site.register(Cargo)
admin.site.register(Estadoaprovacion)
admin.site.register(Document)
admin.site.register(Evento)
admin.site.register(Eventos_en_Permisos)
admin.site.register(Sexo)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Centrocosto)
admin.site.register(Estamento)
admin.site.register(Jefatura)
admin.site.register(Nacionalidad)
admin.site.register(Contrato)
admin.site.register(Funcion)
admin.site.register(Motivo)
admin.site.register(Tipo_Permiso)
admin.site.register(Actividad)
admin.site.register(Bitacora)
admin.site.register(Horas)
admin.site.register(Eventos_en_Permisos_Anulados)
admin.site.register(Anulado)
admin.site.register(Revisor)
admin.site.register(Estado_Permiso)
admin.site.register(Sindicato)
admin.site.register(Estado)
admin.site.register(Licencia)
admin.site.register(TipoLicencia)
admin.site.register(TipoReposo)
admin.site.register(EspecialidadMedica)





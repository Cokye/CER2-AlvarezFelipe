from django.contrib import admin
from core.models import Comunicado,Categoria

# Register your models here.

class ComunicadoAdmin(admin.ModelAdmin):
    pass

class CategoriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comunicado,ComunicadoAdmin)   # Permite gestionar la tabla carreras
admin.site.register(Categoria,CategoriaAdmin)  

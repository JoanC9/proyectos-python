from django.contrib import admin       #importamos las tablas que creamos en models
from gestion.models import Trabajador,Postulante,Despedido

# Register your models here.

#creamos estas clases con nombre como referencias a las tablas para que sea intuitivo
#le colocamos pasamos como atributo lo de admin y adentro le colocamos las
#demas cosas que podemos usar estod sirve en el panel de admin de django
class AdminTrabajador (admin.ModelAdmin):
    
    list_display = ('nombre','apellido','realiza','numero',)
    search_fields = ('nombre','apellido','realiza',)
    list_filter = ('numero',)
    
class AdminPostulante (admin.ModelAdmin):
    
    list_display = ('nombre','ciudad','codigo',)
    search_fields = ('nombre','ciudad','codigo',)
    list_filter = ('ciudad',)
    
class AdminDespedido (admin.ModelAdmin):
    
    list_display = ('nombre','fecha','pagado',)
    search_fields = ('nombre',)
    list_filter = ('pagado',)
    date_hierarchy = 'fecha'

#asi registramos nuestras vistas y como segundo parametro debemos pasar las clases de arriba
admin.site.register(Trabajador,AdminTrabajador)
admin.site.register(Postulante,AdminPostulante)
admin.site.register(Despedido,AdminDespedido)
from django.urls import path    #A ESTEARCHIVO SE REMITE EL URL padre
from gestion.views import buscar,encuentra,inicio,contacto #Asi importamos las vistasde views

urlpatterns = [
    
    #se deja vacio con eso el primero que aparece al inicio del servidor es el inicio
    path('',inicio),
    path('buscar/',buscar),
    path('encuentra/', encuentra),
    path('contacto/', contacto)
]
from django.db import models

# Create your models here.

#cada clase signifca una tabla en la bd haciendo uso de models le especificamos
#que tipo de campo debe ser ES ACONSEJABLE COLOCAR UN STR SIEMPRE
class Trabajador (models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    realiza = models.CharField(max_length=30, verbose_name='Desenpeña')
    numero = models.BigIntegerField()
    tfn = models.BigIntegerField(blank=True,null=True)
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} {self.realiza}. Numero: {self.numero}'
    
class Postulante (models.Model):
    
    nombre = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    codigo = models.IntegerField(verbose_name='Codigo Postal', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.nombre}. Ciudad: {self.ciudad}'
    
class Despedido (models.Model):
    
    nombre = models.CharField()
    fecha = models.DateField(verbose_name='Fecha Despido')
    pagado = models.BooleanField(verbose_name='Todo Al Día')
    
    def __str__(self) -> str:
        return f'{self.nombre}. Fecha: {self.fecha}.'

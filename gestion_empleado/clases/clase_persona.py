#del modulo abc importa la clase y trae una clase auxiliar de ABC, o sea abstrac es una meta clase de ABC 
from abc import ABC, abstractclassmethod

#aca creamos una clase plantilla la cual sirve para heredar y que sus hijas si o si cumplan con estos requisitos
class Persona(ABC):
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    @abstractclassmethod
    def __str__(self) -> str:
        pass
    
#clase que hereda de plantilla y implementa el metodo especial str junto a un nuevo atributo 
class Empleado(Persona):
    
    def __init__(self, nombre, edad,pago):
        super().__init__(nombre, edad)
        
        self.pago = pago
        
    def __str__(self) -> str:
        return f"""Datos del empleado:
                    Nombre: {self.nombre}
                    Edad: {self.edad}
                    Sueldo: {self.pago.sueldo:.2f}
                    Bono: {self.pago.bono:.2f}
                    Sueldo con bono: {self.pago.sueldo_con_bono:.2f}\n"""
    
    
        
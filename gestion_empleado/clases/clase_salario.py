#Clase que crea un atributo de instancia muy privado
class Salario:
    
    def __init__(self,sueldo):
        
        self.__sueldo = sueldo
    
    #metodo que retorna el atributo muy privado
    @property
    def sueldo (self):
        return self.__sueldo
    
    #metodo que saca el valor de bono en base al atributo privado y lo retorna 
    @property 
    def bono (self):
        
        bono = 10 / 100 * self.__sueldo
        
        return bono
    
    #metodo que retorna el valor de sueldo mas bono
    @property   
    def sueldo_con_bono (self):
        
        sueldo_final = self.__sueldo + self.bono
        
        return sueldo_final
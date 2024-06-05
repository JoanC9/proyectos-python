#clase que se encarga de sumar los sueldos de los empleados
class SueldosEmpleado:
    
    #recibe como parametro una lista y lo igualamos atributo 
    def __init__(self,lista_de_empleados):
        
        self.lista = lista_de_empleados
        
    #metodo que suma los sueldos de los empleados    
    def sumar_sueldo (self):
        
        #creamos una lista
        lista_suma_sueldos = []
        
        #iteramos sobre la lista que recibimos como parametro y lo agregamos a la lista de arriba
        for sueldos in self.lista:
            
            if sueldos.pago.sueldo:
                lista_suma_sueldos.append(sueldos.pago.sueldo)
        
        #si lista sueldos no esta vacia entra aca y sumas todo y lo retornas
        if lista_suma_sueldos:  
            suma_sueldos = sum(lista_suma_sueldos)     
            print(f"La suma de los sueldos de todos los empleados es: {suma_sueldos:.2f}")
            print()
        
        #de lo contrario retorna este mensaje    
        else:
            print("La suma no se puede realizar porque la lista esta vacia.\n")
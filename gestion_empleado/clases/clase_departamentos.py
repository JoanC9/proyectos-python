#creamos una lista para almacenar a los empeados
lista_empleados = []

#clase que se encarga de las operaciones de la la lista operaciones generales
class OperacionesLista:
    
    #como agregar un empleado
    def agregar_empleado (self,empleado):
        
        lista_empleados.append(empleado)
          
    #o mostrar a todos los empleados      
    def mostrar_lista (self):
        if lista_empleados:
            
            for indice, empleado in enumerate(lista_empleados):
                print(f"Posicion: {indice + 1}.\n{empleado}")
                
        else:
            print("Lista vacia.\n")
              
    #devolver la lista empleados          
    def devolver_lista(self):
        return lista_empleados
    
#hereda de operaciones lista asi que cumple con el principio I o sea el de barbara Liskov
class Departamento(OperacionesLista):
    
    #buscamos a un empleado y para eso recibimos como parametro el nombre
    def buscar_empleado(self,nombre):
        
        #lista que almacena los empleados encontrados
        empleados_encontrados = []
        
        #Iteramos sobre la lista empleados principal
        for empleado in lista_empleados:
            
            #cuando encuentre un nombre igual al que le pasamos por parametro lo agrega a la lista empleados encontrados
            if empleado.nombre.lower() == nombre.lower():
                
                empleados_encontrados.append(empleado)
        
        #si la lista de empleados encontrados no esta vacia entra aca de lo contrario imprime else
        if empleados_encontrados:
            
            print(f"Los empleados encontrados son:\n")
            #itera sobre la lista de empleados encontrados y devuelve el str del objeto empleado 
            for empleado in empleados_encontrados:
                
                print(f"{empleado}\n")
        else:
            print("No se encontro ningun empleado\n")
    
    #funcion que elimina un empleado y para eso recibe como parametro el nombre del empleado     
    def elimiar_empleado(self,nombre):
        
        empleados_encontrados = []  # Lista para almacenar empleados encontrados

        #iteramos sobre la lista empleado la principal y si el nombre coincide con el introducido como parametro
        #entonce lo agrega a la lista empleados con su respectivo indice
        for indice, empleado in enumerate(lista_empleados):
            if empleado.nombre.lower() == nombre.lower():
                empleados_encontrados.append((indice, empleado))

        #si empleados encontrados no esta vacia retorna la lista con su indice y se le suma 1 para que no empiece desde 0
        if empleados_encontrados:
            print("Empleados encontrados con ese nombre: ")
            for indice, empleado in empleados_encontrados:
                print(f"Indice: {indice+1}\n {empleado}")
            
            # Lógica para eliminar empleado de la lista original 
            while True:
                
                #se le pide que ingrese el indice 
                opcion = input("Ingrese el número de índice del empleado que desea eliminar: ")
                
                #en un bloque try pasamos lo introducido a intero y le restamos 1  ya que en programacion se cuenta desde 0
                try:
                    opcion = int(opcion)
                    opcion = opcion - 1
                    
                    # si la opcion es mayor o igual a 0 y aparte es menor que la longitud de la lista imprime este mensaje 
                    #y termina el bucle while
                    if opcion >= 0 and opcion < len(lista_empleados):
                        lista_empleados.pop(opcion)
                        print("Empleado eliminado correctamente.\n")
                        break
                    
                    #de lo contrario indica que se equivoco y se le da la opcion de intentar otra vez o salir
                    else:
                        print("Índice fuera de rango. No se eliminó ningún empleado.")
                        cancelar = input("O Escriba ´salir` si desea cancelar la operacion o ´continuar` para seguir: ").lower()
                        
                        #se hace un break o un continue segun sea lo que elija
                        if cancelar == "salir":
                            break
                        
                        if cancelar not in ["continuar"]:
                            
                            print("Lo ingresado no es una opcion proporcionada.\n")
                            continue
                        continue
                
                #si lo introducido no es un numero  se le da la opcion de salir o volverlo a intentar  
                except ValueError:
                    print("Por favor, ingrese un número válido.\n")
                    
                    cancelar = input("¿Desea cancelar la operación?. Escriba: ´si` o ´no`\n").lower()
                        
                    if cancelar == "si":
                        break
                    
                    if cancelar not in ["no"]:
                        print("Lo ingresado no es una opcion proporcionada.\n")
                        continue
                    continue
                
        # en caso de que no se encuentren al iterar jejej
        else:
            print("No se encontraron empleados con ese nombre.\n")
    
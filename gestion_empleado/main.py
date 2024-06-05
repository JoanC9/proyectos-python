#Miercoles 1 de mayo 2024
#6:06 pm
#Finaliza este codigo
#Ingeniero Joan Cruz


#Util para importar directorios y modulos internos
import sys

#util para manejar rutas de archivos
import os

#nos almacena la ruta del directorio principal de este modulo
directorio_actual = os.path.dirname(os.path.abspath(__file__))

#concatenamos la ruta de este directorio con cualquier otro directorio que este en el directorio padre
sys.path.append(os.path.join(directorio_actual,".."))

#importamos desde el directorio gestionempleado.subdirectorio clases import modulos a usar y los renombramos as
from gestion_empleado.clases import clase_salario as CS 
from gestion_empleado.clases import clase_persona as CP
from gestion_empleado.clases import clase_departamentos as CD
from gestion_empleado.clases import clase_suma_sueldos as CSS


#funcion que crea un objeto de la clase empleado
def crear_empleado():
    
    #por medio de un bucle while verificamos si los valores introducciodos son correctos
    while True:
        nombre = input("Escribe el nombre: ")

        #con un bloque try nos aseguramos de manejar las excepciones
        try:
            
            edad = int(input("Escribe la edad: "))
            
            # si lo introducido en edad es menor o igual a 17 o menor o igual a 20 pass pero si no imprime mensaje
            #que no se puede tener empleado de esa edad
            if 17 <= edad <= 70:
                pass
            else:
                print("No se puede tener un empleado con esa edad.\n")
                continue
            
            sueldo = float(input("Escribe el salario: "))
            
            #si el sueldo no es mayor o igual a 0 impreme mensaje de que debe pagar a los empleado
            if sueldo >=0:
                pass
            else:
                print("No tenes esclavos :D\n")
                continue
            
            #convierte lo introducido en sueldo a un objeto de la clase salario y lo almacena en una variable
            salario = CS.Salario(sueldo)
            
        #En caso de introducir letras o caracteres especiales imprime este mensaje
        except ValueError:
            print("Debes escribir solo numeros en el apartado de edad y salario.\n")
            continue
        break
    
    #restorna un objeto de la clase empleado y lo atributos son: nombre,edad y objeto de la clase salario
    return CP.Empleado(nombre,edad,salario)

#mensaje de bienvenidad explicando brevemente de que va el programa
print("Bienvenido, este es un programa que te ayuda a gestionar de forma optima a tus empleados.\n")

#Bucle while donde se almacena toda la logica del programama
while True:
    
    print("Escribe el numero de la opcion que quieras realizar")
    
    #bloque try que se encarga de que lo introducido sea de tipo int
    try:
        entrada_usuario =  int(input("1.Crear un empleado\n2.Mostrar lista de empleados\n3.Buscar Empleado\n4.Eliminar Empleado\n5.Mostrar suma sueldos de empleados\n6.salir\n"))
    except ValueError:
        
        print("Escribe solo numeros.\n")
        continue
    
    #analiza si la entreda del usuario es 6 para terminar el programa
    if entrada_usuario == 6:
        print("Hasta luego")
        break
    
    #si la entrada del usuario no es una de las opciones brindadas le dice que escriba una opcion valida y continue
    if entrada_usuario not in [1,2,3,4,5]:
        print("Opcion digitada equivocada.\n")
        continue
    
    #creamos un objeto de la clase departamento
    empresa = CD.Departamento()
    
    #si la entrada del usuario es 1 entra aca
    if entrada_usuario == 1:
        
        #hacemos uso de la funcion crear empleado y lo retornado lo almacenamos en una variable objeto
        objeto = crear_empleado()
        
        #bucle while que nos ayuda a gestionar si el objeto empleado recien creado debe ser guardado
        while True:
            
            #le brindamos al usuario una serie de opciones para escoger
            print("Guarda el empleado en la  en la empresa o si no se va a perder")
            guardar_empleado = input("Escribe ´si` si quieres guardar el empleado o ´no` para salir: ").lower()
            
            #si lo introducido es no terminamos este bucle while y volvemos al bucle principal 
            if guardar_empleado == "no":
                print("Tu empleado se ha perdido\n")
                break
            
            #si lo introducido no es una de las opciones suministradas le decimos que continue a este bucle
            if guardar_empleado not in ["si","no"]:
                print("Opcion digitada equivocada\n")
                continue
            
            # si la opcion es si entra acá
            if guardar_empleado == "si":
                
                #usamos los metodos de la instancia de la clase empresa y como atributo le pasamos el objeto de la clase empleado
                #impreme mensaje de realizado con exito y termina este bucle y vuelve al principal
                empresa.agregar_empleado(objeto)
                
                print("Empleado agregado con exito.\n")
        
                break
    
    #si la opcion digitada es 2 =  mostrar lista   
    if entrada_usuario == 2:
        
        #intancia de la clase lista metodo a usar mostrar lista
        empresa.mostrar_lista()
    
    #si la opcion es 3 = buscar empleador 
    if entrada_usuario == 3:
        
        #almacena lo retornado en metodo devolver lista para asi saber si la lista esta vacia o no
        lista_emp = empresa.devolver_lista()
        
        #si la lista no esta vacia entra aca
        if lista_emp:
            
            #se le pide al usuario escribir el nombre del empleado que quiera buscar
            buscar = input("Escribe el nombre del empleado que quieres buscar: ")

            #y mediante el objeto de la clase empleado haciendo uso del metodo buscar le pasamos como parametro lo escrito para asi buscar
            empresa.buscar_empleado(buscar)
            
        #si la lista esta vacia imprime un mensaje indicandolo
        #esto se hace para cumplir el principio I de solid el cual trata de no mostrar al usuario una interfaz que no necesita
        else:
            print("La lista esta vacia por lo cual no puedes buscar a un empleado.\n")
    
    #si la opcion es 4 = eliminar a un empleado        
    if entrada_usuario == 4:
        
        #lo mismo de arriba almacenamos en una variable lo retornado en lista para saber si esta vacia o no
        #y asi cumplir con el principio I
        listas_emple = empresa.devolver_lista()
        
        #si la lista no esta vacia entra aca
        if listas_emple:
            
            #se le pide al usuario introducir a la persona que quiere eliminar 
            eliminar = input("Escribe el nombre del empleado que quieras eliminar: ")
            
            # y usando el metodo eliminar empleado y como parametro lo introducido se elimina
            empresa.elimiar_empleado(eliminar)
            
        #si esta vacia entra aca
        else:
            print("La lista esta vacia por lo cual no puedes eliminar a un empleado.\n")
    
    #si lo introducido es 5 = sumar sueldos empleados        
    if entrada_usuario == 5:
        
        #almacenamos en una variable lo retornado del metodo 
        lista_empleados = empresa.devolver_lista()
        
        #y en otra variable almacenamos lo retornado de la clase sueldosempleados que se le paso por atributo
        #la lista de empleados
        sueldos_totales = CSS.SueldosEmpleado(lista_empleados)

        # y aca usamos usamos el metodo sumar sueldos para imprimir la suma total de todos los sueldos
        sueldos_totales.sumar_sueldo()

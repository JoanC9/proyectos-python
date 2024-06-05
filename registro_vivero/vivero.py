#Libreria pandas usada para manejar datos y df
import pandas as pd

#Esta biblioteca visualiza datos de forma grafica pylot es un modulo especifico
import matplotlib.pyplot as plt

#libreria sirve para hacer graficos estadisticos
import seaborn as sns 

#Ingeniero Joan Cruz

#ruta donde guardamos el archivo csv
ruta = "ZeroPoo\\aaprendido_final\\registro_vivero\\viverocsv.csv"

# Cargar el DataFrame desde el archivo CSV si existe, de lo contrario, crear uno vacío
try:
    df = pd.read_csv(ruta)
    #Filenot indica si no encuentra la rta del archivo o sea si da error el de arriba
except FileNotFoundError:
    df = pd.DataFrame(columns=["Planta", "PrecioCompra", "PrecioVenta","UnidadCompradas","UnidadVendidas"])

#Mensaje informativo general del programa
print("Programa que ayuda administrar las plantas en un vivero.\nElaborado por: Ing Joan Cruz")

#Bucle donde se almacena toda la logica del programa
while True:
    
    #bloque try donde se le dan unas opciones al usuario a realizar
    try:
        entrada = int(input("\n1. Agregar.\n2. Actualizar.\n3. Buscar.\n4. Mostrar todo el df.\n5. Eliminar.\n6. Contabilidad.\n7. Grafico.\n8. Guardar en archivo excel.\n9. Salir.\n"))
    except ValueError:
        print("Los valores introducidos deben ser de tipo numerico.\n")
        continue
    
    #opcion de finalizar programa
    if entrada == 9:
        print("Hasta luego.")
        break
    
    #condicional en caso de que lo introducido sea numero pero no una opcion proporcionada
    if entrada not in [1,2,3,4,5,6,7,8]:
        print("Numero introducido no corresponde con las opciones suministradas.\n")
        continue
    
    #opcion 1 que sirve para agregar una planta
    if entrada ==1:
        
        # Solicitar los datos al usuario
        a = input("Planta: ").capitalize()
        
        #condicional que analiza si esa planta ya esta en el df 
        if a.lower() in df['Planta'].str.lower().values:
            
            print("Esta planta ya esta en el df. Elije la opcion de actualizar para modificar la informacion.\n")
            
            continue
        
        #bloque try y adentro while que rectifica que lo introducido sea numeros y mayores a 0
        try:
            
            while True:
                
                b = float(input("Precio de compra: "))
                c = float(input("Precio de venta: "))
                
                #se usa or y no and ya que aca se dice si b o c son menores a 0 reinicia
                #si fuera and seria si b y c por lo cual deberian ser los dos menores a 0 y no uno solo como con or
                if b < 0 or c < 0:
                    print("\nNo se puede tener valores negativos en precio.")
                    continue
                
                else:
                    break
                
            while True:
                d = int(input("Unidades Compradas: "))
                e = int(input("Unidades vendidas: "))
                
                if e > d:
                    print("No puedes vender mas de lo que compraste.\n")
                    continue
                else:
                    break
                
        except ValueError:
            print("Todos los precios y las unidades deben ser valores numericos.\n")
            continue

        # Crear un nuevo DataFrame con los datos ingresados
        nuevos_datos = pd.DataFrame({"Planta": [a], "PrecioCompra": [b], "PrecioVenta": [c], "UnidadCompradas": [d], "UnidadVendidas": [e]})
        
        # Concatenar el nuevo DataFrame con el DataFrame existente
        df = pd.concat([df, nuevos_datos], ignore_index=True)

        # Guardar el DataFrame actualizado en el archivo CSV
        df.to_csv(ruta, index=False)

        print("Datos añadidos y guardados correctamente.\n")
    
    #opcion 2 que actualiza el df   
    if entrada == 2:
        
        #encargado de analizar si el df no esta vacio y asi cumplir con el principio I de solid
        if not df.empty:
            
            planta_a_actualizar = input("Escribe el nombre de la planta que desea actualizar: ")

            #condicional que analiza si la planta de verdad esta en el df
            if planta_a_actualizar.lower() in df['Planta'].str.lower().values:
                
                #se trae toda la las columnas pertenecientes a ese fila donde esta planta
                planta_seleccionada = df.loc[df['Planta'].str.lower() == planta_a_actualizar.lower()]
    
                # Imprimir los datos de la planta seleccionada
                print(planta_seleccionada)

                #bucle que almacena la logica para que lo actualizado cumpla con el tipo que debe ser
                while True:
                
                    campo = input("Introduce el campo que deseas actaulizar: ")

                    #condicional que analiza si el campo actualizar es correcto
                    if campo not in ["Planta", "PrecioCompra", "PrecioVenta","UnidadCompradas","UnidadVendidas"]:
                    
                        print("Los campos disponible son: 'Planta', 'PrecioCompra', 'PrecioVenta', 'UnidadCompradas', 'UnidadVendidas.\n Introduce un campo correcto, revisa la ortografia.\n")
                        continue
                
                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                
                    #condicional que dependiendo el campo modifica el tipo de dato
                    if campo in ["PrecioCompra", "PrecioVenta"]:
                        valor = float(nuevo_valor)
                    
                    elif campo in ["UnidadCompradas","UnidadVendidas"]:
                        valor = int(nuevo_valor)

                        #condicional que se encarga de verificar que las plantas vendidas sean menores a las compradas
                        #se coloca values[0] en caso de que exista otra columna con ese nombre para tomar solo la primera
                        if campo == "UnidadVendidas" and valor > planta_seleccionada['UnidadCompradas'].values[0]:
                            print("¡Error! El número de unidades vendidas no puede ser mayor que el número de unidades compradas.\n")
                            continue
                    
                    else:
                        valor = str(nuevo_valor)

                    #la nueva planta se introduce con la primera en mayuscula ya que todas en el df la 1 es mayuscula
                    #y asi nos aseguramos de que no crea que es otra planta y asi la sobreescribimos en el df
                    df.loc[df['Planta'] == planta_a_actualizar.capitalize(), campo] = valor
    
                    # Guardar el DataFrame actualizado en el archivo CSV
                    df.to_csv(ruta, index=False)
                    print("Datos actualizados correctamente.\n")

                    #mensaje y condicionales encargados de analizar en caso de que quiera actualizar
                    #otro valor pero de la misma planta
                    volver_actualizar = input("¿Desea volver actualizar otro valor?. Responda: 'si' o 'no'.\n").lower()
                
                    if volver_actualizar == "si":
                        continue
                
                    elif volver_actualizar == "no":
                        break
                    else:
                        print("Lo introducido no es una de las opciones sumistradas por lo cual se entiende por un no.\n")
                        break
                
            else:
                print("La planta especificada no existe en el registro.\n")
        
        else:
            print("El Dataframe esta vacio.")
    
    #opcion 3 planta que quiera buscar
    if entrada == 3:
        
        #analiza si el df esta vacio
        if not df.empty:
            
            planta_a_actualizar = input("Escribe el nombre de la planta que desea buscar: ")

            #condicional que busca por el nombre de planta con un .lower() para que compare cuando esten en minusculas
            if planta_a_actualizar.lower() in df['Planta'].str.lower().values:
                
                #en caso de que este almacena la planta en una variable
                planta_seleccionada = df.loc[df['Planta'].str.lower() == planta_a_actualizar.lower()]
    
                # Imprimir los datos de la planta seleccionada
                print(planta_seleccionada)
            
            #si no la encuentra imprime este mensaje
            else:
                print("La planta especificada no existe en el registro.\n")
                
        else:
            print("El Dataframe esta vacio.")
        
    #opcion 4 muestra todo el df       
    if entrada == 4:
        
        #si el df no esta vacio lo imprime o si no imprime mensaje
        if not df.empty:
        
            print(df)
        
        else:
            print("El Dataframe esta vacio.")
    
    #opcion 5 eliminar una planta  
    if entrada == 5:
        
        #analiza si el df no esta vacio
        if not df.empty:
        
            planta_a_eliminar = input("Escribe el nombre de la planta que deseas eliminar: ")

            # Convertir el nombre de la planta a minúsculas para una comparación insensible a mayúsculas y minúsculas
            planta_a_eliminar = planta_a_eliminar.lower()

            # Verificar si la planta existe en el DataFrame
            if planta_a_eliminar in df['Planta'].str.lower().values:
                
                # Eliminar todas las filas donde el nombre de la planta coincide con la planta a eliminar
                df = df[df['Planta'].str.lower() != planta_a_eliminar]
    
                # Guardar el DataFrame actualizado en el archivo CSV
                df.to_csv(ruta, index=False)
    
                print(f"Se ha eliminado la planta '{planta_a_eliminar}'.")
            else:
                print("La planta especificada no existe en el registro.")
                
        else:
            print("El Dataframe esta vacio.")
    
    #opcion 6 contabilidad 
    if entrada == 6:
        
        #analiza si el df no esta vacip
        if not df.empty:
            
            #bucle que almacena la logica para sacar los diferentes tipos de contabilidad
            while True:
                print("Escribe el numero de alguna de las siguientes opciones.")

                #try que asegura que lo introducido se una opcion sumistrada
                try:
                    entrada_contabilidad = int(input("\n1. Contabilidad general.\n2. Contabilidad de una planta especifica.\n3. Volver menu inicio\n"))
                
                except ValueError:
                
                    print("Introduzca solo numeros.\n")
                    continue
                    
                #finaliza este bucle
                if entrada_contabilidad == 3:
                    break
                    
                #condicional que analiza en caso que lo introducido no sea una opcion sumistrada
                if entrada_contabilidad not in [1,2]:
                    print("Lo introducido no es una opcion suministrada.\n")
                
                #condicional que almacena la logica de la contabilidad general
                if entrada_contabilidad == 1:
                    
                    #por increible que parezca esto multiplica los valore de su respectiva fila
                    
                    # Calcular el total invertido en la compra para cada planta
                    df['TotalCompra'] = df['PrecioCompra'] * df['UnidadCompradas']

                    # Calcular el total obtenido por la venta para cada planta
                    df['TotalVenta'] = df['PrecioVenta'] * df['UnidadVendidas']

                    # Calcular el total invertido y el total obtenido
                    total_invertido = df['TotalCompra'].sum()
                    total_obtenido = df['TotalVenta'].sum()

                    # Calcular las ganancias
                    ganancias = total_obtenido - total_invertido

                    #imprime resultados
                    print(f"\nTotal invertido en la compra: {total_invertido}")
                    print(f"Total obtenido por la venta: {total_obtenido}")
                    print(f"Ingreso bruto: {ganancias}\n")
                
                #condicional en caso que quiera la contabilidad de una sola planta
                if entrada_contabilidad == 2:
                    planta_seleccionada = input("\nIntroduce el nombre de la planta: ")

                    # Convertir el nombre de la planta a minúsculas para una comparación insensible a mayúsculas y minúsculas
                    planta_seleccionada = planta_seleccionada.lower()

                    # Verificar si la planta seleccionada está presente en el DataFrame
                    if planta_seleccionada in df['Planta'].str.lower().values:
                        # Filtrar el DataFrame para obtener solo la fila correspondiente a la planta seleccionada
                        planta_df = df[df['Planta'].str.lower() == planta_seleccionada]
    
                        # Calcular el total invertido en la compra para la planta seleccionada
                        total_invertido_planta = planta_df['PrecioCompra'] * planta_df['UnidadCompradas']
    
                        # Calcular el total obtenido por la venta para la planta seleccionada
                        total_obtenido_planta = planta_df['PrecioVenta'] * planta_df['UnidadVendidas']
    
                        # Calcular las ganancias para la planta seleccionada
                        ganancias_planta = total_obtenido_planta.sum() - total_invertido_planta.sum()
    
                        # Imprimir los resultados
                        print("Total invertido en la compra:", total_invertido_planta.sum())
                        print("Total obtenido por la venta:", total_obtenido_planta.sum())
                        print("Ganancias:", ganancias_planta)
                    else:
                        print("La planta especificada no existe en el registro.\n")
                        
        else:
            print("El Dataframe esta vacio.")
    
    #opcion 7 que muestra graficos              
    if entrada == 7:
        
        #analiza si el df no esta vacio
        if not df.empty:
            
            #bucle que contiene toda la logica donde se le muestra al usuario 2 opciones de grafico
            while True:
                
                #try que analiza que lo introducido sea numero
                try:
                    
                    elegir_grafico = int(input("\n1. Grafico de plantas mas vendidas.\n2. Grafico de plantas mas compradas.\n3. Volver al menu principal.\n"))
                
                except ValueError:
                    
                    print("Escriba solo el numero de las opciones proporcionadas.")
                    continue
                
                #Termina este bucle
                if elegir_grafico == 3:
                    break
                
                #analiza si lo introducido no es una opcion
                if  elegir_grafico not in [1,2]:
                    print("Numero introducido no es un opcion suministrada.")
                    break
                
                #condicional que contiene la logica del primer grafico de barras
                if elegir_grafico == 1:
                    
                    #este grafico es igual al de abajo solo cambia el eje y 
                    #aca le decimos cual es el eje x, y los datos los tomas del df los colores o palette sera eston y quiero una leyenda 
                    sns.barplot(x="Planta", y="UnidadVendidas", data=df, hue="Planta", palette='hls', legend=True)
                    
                    #mostramos el grafico con esto
                    plt.show()
                
                #condicional que contiene la logica del segundo grafico  
                elif elegir_grafico == 2:
                    
                    sns.barplot(x="Planta", y="UnidadCompradas", data=df, hue="Planta", palette='hls', legend=True)
                    plt.show()
                    
        else:
            print("El DataFrame está vacío.")
    
    #opcion 8 que guarda el dataframe como excel      
    if entrada == 8:
        
        #si el df no esta vacio
        if not df.empty:
            
            #le asignamos una ruta y como se debe llamar
            ruta_excel = "ZeroPoo\\aaprendido_final\\registro_vivero\\viveroexcel.xlsx"
            
            #y lo guardamos como csv pero ahora se to_excel
            df.to_excel(ruta_excel, index= False)
            
            #mensaje de guardado correcto
            print("Guardado en formato excel correctamente.")
            
        else:
            print("El DataFrame esta vacio.")

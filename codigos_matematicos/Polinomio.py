import numpy as np  # Importamos la librería NumPy y le asignamos el alias np

#REALIZADO POR: JOAN EMMANUEL CRUZ LOPEZ

# # Definimos los datos como arreglos de NumPy
t = np.array([0.8, 3.8, 6.8, 9.8, 12.8, 15.8]) # Valores de t(s)
h = np.array([34.3652,144.1568,220.2248,262.8458,272.2768,247.7598])   # Valores de h(m)

# Función para calcular el polinomio de interpolación de Lagrange
def lagrange_interpolation(t, h, x):
    
    """
    Calcula el polinomio de interpolación de Lagrange para los datos dados.

    :param t: Array de valores de t.
    :param h: Array de valores de h.
    :param x: Valor específico de t para calcular h.
    :return: El valor interpolado de h para el valor de t dado.
    """
    
    n = len(t)  # Obtenemos la cantidad de puntos de datos (longitud de t)
    result = 0.0    # Inicializamos el resultado del polinomio de interpolación
    
    # Iteramos sobre los índices de t
    for i in range(n):
        
        term = h[i] # Inicializamos el término del polinomio de Lagrange con el valor de h correspondiente
        
        # Iteramos nuevamente para calcular el término del polinomio de Lagrange
        for j in range(n):
            
            if j != i: # Nos aseguramos de no incluir el mismo punto en el cálculo del término
                
                # Explicación: La expresión (x - t[j]) / (t[i] - t[j]) garantiza que el término sea 0 en todos los puntos
                # excepto en t[i], donde es igual a 1. Esto asegura que el término del polinomio de Lagrange sea 0 en
                # todos los puntos, excepto en el punto t[i], donde es igual a h[i].
                term *= (x - t[j]) / (t[i] - t[j])
                
        result += term # Sumamos el término calculado al resultado acumulado
        
    return result # Retornamos el valor interpolado de h para el valor de t dado


#ESTO PERTENECE AL PUNTO 1.B

# Calcular el polinomio de interpolación para un valor específico de t empezando desde 0
t_interpolation = 0.8

#le asignamos el valor de 1 ya que esta variable es la que nos va indicar el total de datos
indice = 1

#Dentro de un bucle hacemos que imprima la lista de los datos se debían haber recibido
while True:
    
    #usamos la funcion que creamos y le pasamos los valores de t, h y el valor especifico
    h_interpolation = lagrange_interpolation(t, h, t_interpolation)
    
    #nos imprime el mensaje con el h(m) correspondiente y 4 decimales
    print(f"{indice}. Para t = {t_interpolation}. h es aproximadamente {h_interpolation:.4f}\n")
    
    #y aumentamos 1 ya que especifica que en intervalos de 1 segundo
    t_interpolation += 1
        
    #y cuando ya tengamos 25 datos termina el bucle
    if indice == 25:
        break
    
    #aumentamos el indice de 1 en 1 despues de imprimir cada mensaje
    indice +=1

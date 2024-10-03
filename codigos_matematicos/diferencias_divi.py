# Importamos la biblioteca NumPy, que nos permite realizar cálculos numéricos de manera eficiente
import numpy as np

# Definimos los datos de entrada
x_values = np.array([-7, 0, 5, 9])  # Valores de x
y_values = np.array([0, -1, 2, 1])  # Valores de y correspondientes a cada x

# Definimos una función para calcular las diferencias divididas
def divided_differences(x, y):
    """
    Calcula las diferencias divididas para un conjunto de puntos (x, y).
    
    Parámetros:
    x (numpy.array): Valores de x
    y (numpy.array): Valores de y correspondientes a cada x
    
    Retorna:
    coefficients (numpy.array): Coeficientes de la forma de Newton
    """
    n = len(x)  # Número de puntos
    F = np.zeros((n, n))  # Matriz para almacenar las diferencias divididas
    
    # Inicializamos la primera columna de la matriz con los valores de y
    for i in range(n):
        F[i, 0] = y[i]

    # Calculamos las diferencias divididas para cada columna
    for j in range(1, n):
        for i in range(j, n):
            # Fórmula para calcular la diferencia dividida
            F[i, j] = (F[i, j - 1] - F[i - 1, j - 1]) / (x[i] - x[i - j])

    # Retornamos la diagonal principal de la matriz, que contiene los coeficientes
    return F.diagonal()

# Calculamos las diferencias divididas para nuestros datos
coefficients = divided_differences(x_values, y_values)

# Extraemos el coeficiente a2
a2 = coefficients[2]

# Imprimimos el resultado
print("El coeficiente a2 es:", a2)
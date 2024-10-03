import numpy as np
from scipy.interpolate import lagrange

# Datos de entrada
x_data = np.array([0, 1, 2, 3])
y_data = np.array([3, 2, 4, -1.9])

# Polinomio de interpolación de Lagrange
poly = lagrange(x_data, y_data)

# Derivada del polinomio
poly_derivative = np.polyder(poly)

# Encontrar las raíces de la derivada (máximos y mínimos locales)
roots = np.roots(poly_derivative)

# Filtrar las raíces que se encuentran dentro del rango de los datos originales
max_local_x = [root.real for root in roots if min(x_data) <= root.real <= max(x_data)]

# El máximo local será la raíz más grande encontrada
max_local_x = max(max_local_x)

print("El valor de x donde el polinomio alcanza su máximo local es:", round(max_local_x, 4))
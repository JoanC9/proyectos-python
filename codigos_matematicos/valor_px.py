# Datos
x_values = [1, 2, 3]
y_values = [0, 4.4, 0]

# Interpolación de Lagrange
from scipy.interpolate import lagrange
poly = lagrange(x_values, y_values)

# Cálculo de la integral cúbica utilizando la regla del trapecio
def integral_cubica(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

integral_cubica_valor = integral_cubica(poly, x_values[0], x_values[-1], 1000)

print("El valor de la integral cúbica del polinomio interpolante es:", round(integral_cubica_valor, 4))
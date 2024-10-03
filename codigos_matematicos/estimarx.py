def lagrange_interpolation(x, y, xi):
    """
    Calcula la interpolación polinómica de Lagrange para encontrar el valor de y en xi.

    Argumentos:
    x -- Lista de valores x conocidos
    y -- Lista de valores y conocidos
    xi -- Valor de x para el cual se desea estimar el valor de y

    Retorna:
    yi -- Estimación de y para el valor xi
    """
    yi = 0
    for i in range(len(y)):
        term = y[i]
        for j in range(len(x)):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        yi += term
    return yi


# Datos conocidos
x = [-1, 2, 5, 7, 9]
y = [0, -1, 0, 3, 0]

# Valor para el cual queremos estimar y
xi = 8.4

# Calcula la estimación de y para xi usando interpolación de Lagrange
yi = lagrange_interpolation(x, y, xi)

print("La estimación de la imagen de x =", xi, "es:", round(yi, 4))
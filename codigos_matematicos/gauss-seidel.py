# Importamos la biblioteca NumPy, que nos permite realizar cálculos numéricos de manera eficiente
import numpy as np

# INGRESO
# Definimos la matriz A y el vector B del sistema de ecuaciones
A = np.array([[4.4, 2.9, 8.4],
              [7,  7.4, 5.6],
              [6.2, 3.6, 9.5]])

B = np.array([1.5, 9.7, 1.8])

# Definimos un vector inicial X0 para el método iterativo
X0  = np.array([6.5,9.3,2.9])

# Definimos la tolerancia para el error y el número máximo de iteraciones
tolera = 0.00001
iteramax = 10

# PROCEDIMIENTO
# Método de Gauss-Seidel para resolver el sistema de ecuaciones

# Obtenemos el tamaño de la matriz A
tamano = np.shape(A)
n = tamano[0]  # Número de filas
m = tamano[1]  # Número de columnas

# Inicializamos el vector X con el valor inicial X0
X = np.copy(X0)

# Inicializamos un vector para almacenar las diferencias entre iteraciones
diferencia = np.ones(n, dtype=float)

# Inicializamos un valor para el error máximo
errado = 2*tolera

# Inicializamos el contador de iteraciones
itera = 0

# Bucle para realizar las iteraciones
while not(errado<=tolera or itera>iteramax):
    print('iteración: ',itera+1)
    
    # Bucle para recorrer las filas de la matriz A
    for i in range(0,n,1):
        # Bucle para recorrer las columnas de la matriz A
        suma = 0 
        for j in range(0,m,1):
            # Excepto la diagonal de A
            if (i!=j): 
                suma = suma-A[i,j]*X[j]
        
        # Calculamos el nuevo valor de X[i]
        nuevo = (B[i]+suma)/A[i,i]
        
        # Calculamos la diferencia absoluta entre el nuevo valor y el valor anterior
        diferencia[i] = np.abs(nuevo-X[i])
        
        # Actualizamos el valor de X[i]
        X[i] = nuevo
        
        # Imprimimos el valor de X[i]
        print('X[',i+1,']=',X[i])
    
    # Calculamos el error máximo en esta iteración
    errado = np.max(diferencia)
    
    # Incrementamos el contador de iteraciones
    itera = itera + 1

# Reorganizamos el vector X en una columna
X = np.transpose([X])

# Revisamos si el método no converge
if (itera>iteramax):
    X=0

# Revisamos la respuesta verificando si A.X=B
verifica = np.dot(A,X)

# SALIDA
print('respuesta X: ')
print(X)
print('verificar A.X=B: ')
print(verifica)
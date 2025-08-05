# Crear una lista con los cuadrados de los n primeros números naturales
def cuadrados(n):
    return [i**2 for i in range(1, n+1)]

# Imprimir la lista de cuadrados
print(cuadrados(5))

# Crear una lista con los cubos de los n primeros números naturales
def cubos(n):
    return [i**3 for i in range(1, n+1)]

# Imprimir la lista de cubos
print(cubos(5))
print("Hola, Cursor")

# Este bucle imprime los números del 0 al 4 en la consola
for i in range(5):
    print(i)

# Calcular el factorial de un número dado
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Imprimir el factorial de 5
print(factorial(5))

def suma_lista(lista:list) -> list:
    total = 0
    for i in lista:
        total += i
    return total
"""
    La función suma_lista toma una lista de números y devuelve la suma de los elementos de la lista.
    La función es de tipo list y devuelve un número.
    La función es una función recursiva.
    La función es una función que toma una lista de números y devuelve la suma de los elementos de la lista.    
    """
# Imprimir la suma de la lista
print(suma_lista([1, 2, 3, 4, 5]))


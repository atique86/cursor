# Crear una función que determine si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número para verificar si es primo: "))
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
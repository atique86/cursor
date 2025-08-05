# Crear una calculadora simple que permita realizar operaciones básicas
# 1. Pedir al usuario que ingrese dos números.
# 2. Pedir al usuario que ingrese la operación a realizar.
# 3. Realizar la operación.
# 4. Mostrar el resultado.
# 5. Repetir el proceso hasta que el usuario lo indique.

def solicitar_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def solicitar_operacion():
    operaciones = ['+', '-', '*', '/']
    while True:
        op = input("Ingrese la operación a realizar (+, -, *, /): ")
        if op in operaciones:
            return op
        else:
            print("Operación no válida. Intente de nuevo.")

def calcular(num1, num2, operacion):
    try:
        if operacion == "+":
            return num1 + num2
        elif operacion == "-":
            return num1 - num2
        elif operacion == "*":
            return num1 * num2
        elif operacion == "/":
            return num1 / num2
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None

def main():
    while True:
        numero1 = solicitar_numero("Ingrese el primer número: ")
        numero2 = solicitar_numero("Ingrese el segundo número: ")
        operacion = solicitar_operacion()
        resultado = calcular(numero1, numero2, operacion)
        if resultado is not None:
            print(f"El resultado de la operación es: {resultado}")
        respuesta = input("¿Desea realizar otra operación? (s/n): ").lower()
        if respuesta == "n":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
# 1. Recorrer los números del 1 al 50.
# 2. Si el número es divisible por 3, imprimir "Fizz".
# 3. Si el número es divisible por 5, imprimir "Buzz".
# 4. Si el número es divisible por 3 y 5, imprimir "FizzBuzz".
# 5. Si el número no es divisible por 3 ni 5, imprimir el número.

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
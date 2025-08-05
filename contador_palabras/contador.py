# Programa para contar palabras en un archivo de texto
import re
from collections import Counter

class ContadorDePalabras:
    def __init__(self):
        self.contenido = ""

    def leer_archivo(self, ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as file:
                self.contenido = file.read()
        except FileNotFoundError:
            print(f"El archivo {ruta} no existe.")
            exit()

    def contar_palabras(self, texto=None):
        if texto is None:
            texto = self.contenido
        palabras = re.findall(r'\b\w+\b', texto.lower())
        return len(palabras), palabras

    def palabras_mas_frecuentes(self, palabras, n=10):
        contador = Counter(palabras)
        return contador.most_common(n)

# Test para la función contar_palabras
if __name__ == "__main__":
    # Prueba simple
    texto_prueba = "El oso está en el bosque. El oso duerme."
    contador = ContadorDePalabras()
    total, palabras = contador.contar_palabras(texto_prueba)
    print(f"Test: {total == 9}, palabras encontradas: {total}")

    # Uso interactivo
    ruta = input("Ingrese la ruta del archivo de texto: ")
    contador.leer_archivo(ruta)
    total, palabras = contador.contar_palabras()
    print(f"El archivo tiene {total} palabras.")
    mas_comunes = contador.palabras_mas_frecuentes(palabras)
    print("\nLas 10 palabras más frecuentes:")
    for palabra, conteo in mas_comunes:
        print(f"{palabra}: {conteo}")
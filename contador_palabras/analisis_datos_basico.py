# 1. Importar archivo .csv para analizar
# 2. Analizar los datos del archivo .csv
# 3. Calcular media de cada columna
# 4. Calcular mediana de cada columna
# 5. Calcular desviación estándar de cada columna
# 6. Generar gráfico de dispersión de columna 1 vs columna 2
# 7. Trazar un scatter plot de columna 1 vs columna 2

# 1. Importar archivo .csv para analizar
import pandas as pd
import matplotlib.pyplot as plt

# 2. Analizar los datos del archivo .csv
df = pd.read_csv(r'D:\Platzi\Santander Academy\Cursor\contador_palabras\numeros.csv', sep=';', encoding='utf-8')
df.columns = ['columna1', 'columna2']

# 3. Calcular media de cada columna
media = df.mean()
print(f"Media: {media}")

# 4. Calcular mediana de cada columna
mediana = df.median()
print(f"Mediana: {mediana}")

# 5. Calcular desviación estándar de cada columna
desviacion = df.std()
print(f"Desviación estándar: {desviacion}")

# 6. Generar gráfico de dispersión de columna 1 vs columna 2
plt.scatter(df['columna1'], df['columna2'])
plt.show()

# 7. Trazar un scatter plot de columna 1 vs columna 2
plt.scatter(df['columna1'], df['columna2'])
plt.show()

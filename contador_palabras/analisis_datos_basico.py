# 1. Importar archivo .csv para analizar
# 2. Analizar los datos del archivo .csv
# 3. Calcular media de cada columna
# 4. Calcular mediana de cada columna
# 5. Calcular desviación estándar de cada columna
# 6. Generar gráfico de dispersión de columna 1 vs columna 2
# 7. Trazar un scatter plot de columna 1 vs columna 2

import pandas as pd
import matplotlib.pyplot as plt

def analizar_datos_csv(ruta_archivo):
    """
    Realiza un análisis básico de datos desde un archivo CSV.
    
    Esta función lee un archivo CSV, calcula estadísticas descriptivas
    (media, mediana, desviación estándar) para cada columna y genera
    gráficos de dispersión para visualizar la relación entre las columnas.
    
    Args:
        ruta_archivo (str): Ruta al archivo CSV que se va a analizar.
                           El archivo debe tener dos columnas numéricas
                           separadas por punto y coma (;).
    
    Returns:
        dict: Diccionario con las estadísticas calculadas:
            - 'media': Media de cada columna
            - 'mediana': Mediana de cada columna  
            - 'desviacion': Desviación estándar de cada columna
            - 'dataframe': DataFrame con los datos leídos
    
    Raises:
        FileNotFoundError: Si el archivo CSV no existe en la ruta especificada
        ValueError: Si el archivo no tiene el formato esperado
    
    Example:
        >>> stats = analizar_datos_csv('numeros.csv')
        >>> print(stats['media'])
    """
    # Leer el archivo CSV
    df = pd.read_csv(ruta_archivo, sep=';', encoding='utf-8')
    df.columns = ['columna1', 'columna2']
    
    # Calcular estadísticas descriptivas
    media = df.mean()
    mediana = df.median()
    desviacion = df.std()
    
    # Generar gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(df['columna1'], df['columna2'], alpha=0.7, color='blue')
    plt.title('Gráfico de Dispersión: Columna 1 vs Columna 2')
    plt.xlabel('Columna 1')
    plt.ylabel('Columna 2')
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Retornar estadísticas como diccionario
    return {
        'media': media,
        'mediana': mediana,
        'desviacion': desviacion,
        'dataframe': df
    }

if __name__ == "__main__":
    # Ejecutar el análisis con el archivo por defecto
    ruta_archivo = r'D:\Platzi\Santander Academy\Cursor\contador_palabras\numeros.csv'
    try:
        estadisticas = analizar_datos_csv(ruta_archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
    except Exception as e:
        print(f"Error durante el análisis: {e}")

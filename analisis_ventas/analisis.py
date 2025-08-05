# 1. Cargar datos del CSV y preparar datos
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos y asegurar que 'fecha' sea datetime
df = pd.read_csv(r'D:\Platzi\Santander Academy\Cursor\analisis_ventas\ventas.csv', parse_dates=['fecha'])  # Corregido 'fecha' (había un typo en tu CSV original)

# 2. Calcular ventas totales por mes
df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes').apply(lambda x: (x['cantidad'] * x['precio']).sum())
ventas_por_mes = ventas_por_mes.sort_index()

print("\nVentas por mes:")
print(ventas_por_mes)

# 3. Determinar producto más vendido y con mayor ingresos
df['ingreso'] = df['cantidad'] * df['precio']
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
}).sort_values('ingreso', ascending=False)

mas_vendido = ventas_prod['cantidad'].idxmax()
mayor_ingreso = ventas_prod['ingreso'].idxmax()

print(f"\nProducto más vendido en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'cantidad']} unidades)")
print(f"Producto con mayores ingresos: {mayor_ingreso} (total €{ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f})")

# 4. Graficar ventas por mes (nuevo gráfico añadido)
plt.figure(figsize=(10, 5))
ventas_por_mes.plot(kind='bar', color='skyblue')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Ingresos (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_por_mes.png')
plt.show()

# 5. Graficar top 5 productos por ingresos
top5 = ventas_prod.nlargest(5, 'ingreso')
plt.figure(figsize=(10, 5))
bars = plt.bar(top5.index, top5['ingreso'], color='lightgreen')

# Añadir valores encima de las barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'€{height:,.2f}',
             ha='center', va='bottom')

plt.title("Top 5 Productos por Ingresos")
plt.ylabel("Ingresos (€)")
plt.xlabel("Producto")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top5_productos.png")
plt.show()
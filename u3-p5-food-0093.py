import pandas as pd
import matplotlib.pyplot as plt
# PEDRO MARTINEZ NC 0093
df_food_india = pd.read_csv('indian_food.csv')

print("\n--- DATOS LEÍDOS DESDE CSV, COMIDA INDIA 0093 ---")
print(df_food_india)

print("\nMostrar Nombre comida + ingredientes 0093")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)

print("\n Mostrando los primeros 10 registros PEDRO MARTINEZ NC 0093")
# Se corrigió 'tiempo_de_coccion' por 'cook_time'
Nombre_Tiempo = df_food_india[['name', 'cook_time']].head(10)
print(Nombre_Tiempo)
print("\n grafica comida (X),Tiempo de cocinado(Y) PEDRO MARTINEZ NC 0093")
print("grafica comida (X) texto a 30 grados")
Nombre_Tiempo.plot.bar(x='name',y='cook_time', rot=30)
plt.title("Comida tipica de india Pedro Martinez 0093")
plt.xlabel("Nombre de platillo")
plt.ylabel("Tiempo de cocinado")
plt.show()
print("\n graficas de varias columnas")
Nombre_Tiempo = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
Nombre_Tiempo.plot.bar(x='name', rot=30)
Nombre_Tiempo.plot.bar(x='name', y=['prep_time', 'cook_time'], rot=30)
plt.title("grafica 2 columnas Pedro Martinez 0093")
plt.xlabel("Nombre de platillo")
plt.ylabel("Tiempo de cocinado prep y comida ")
plt.show()
print("\n graficas apiladas verticalmete una tras otra Pedro Martinez NC. 0093")
Nombre_Tiempo.plot.bar(x='name',rot =30 ,stacked=True)
plt.title("Graficas apiladas Pedro Martinez NC 0093")
plt.xlabel("Nombre de platillo")
plt.ylabel("Tiempo de cocinado prep y comida ")
plt.show()
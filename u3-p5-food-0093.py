import pandas as pd
import matplotlib.pyplot as plt
# PEDRO MARTINEZ NC 0093
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV,COMIDA INDIA 0093 ---")
print(df_food_india)
print("Mostrar Nombre comida + ingredientes 0093")
df_food_india = pd.read_csv('indian_food.csv')
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("Mostrando los primeros 10 registros  PEDRO MARTINEZ NC 0093")
Nombre_Tiempo = df_food_india[['name', 'tiempo_de_coccion']].head(10)
print(Nombre_Tiempo)
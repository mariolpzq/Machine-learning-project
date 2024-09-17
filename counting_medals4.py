import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv('olympics_dataset.csv')

# Agrupar por 'Name', 'Team', y 'Year' y contar las medallas de cada tipo
# Usamos .unstack() para convertir las medallas en columnas
medal_counts = df.groupby(['Name', 'Team', 'Year', 'Medal']).size().unstack(fill_value=0)

# Verificar qué columnas se crearon
print(medal_counts.columns)

# Renombrar las columnas de acuerdo a las medallas presentes
# Si las columnas no aparecen en el orden esperado, se pueden ajustar dinámicamente
if 'Gold' in medal_counts.columns and 'Silver' in medal_counts.columns and 'Bronze' in medal_counts.columns:
    medal_counts = medal_counts[['Gold', 'Silver', 'Bronze']]
else:
    # Si las columnas están en otro orden o hay más columnas de lo esperado, ajustamos el renombrado
    medal_counts = medal_counts.rename(columns=lambda x: x.capitalize() if x in ['gold', 'silver', 'bronze'] else x)

# Restablecer el índice para que 'Name', 'Team', y 'Year' sean columnas
medal_counts = medal_counts.reset_index()

# Asegurarnos de incluir a los atletas que no ganaron medallas
# Agrupamos para obtener una lista completa de todos los atletas que participaron
all_athletes = df.groupby(['Name', 'Team', 'Year']).size().reset_index()[['Name', 'Team', 'Year']]

# Hacemos un merge de todos los atletas con el conteo de medallas
complete_counts = pd.merge(all_athletes, medal_counts, on=['Name', 'Team', 'Year'], how='left')

# Rellenar los valores NaN en las columnas de medallas con 0 (para atletas sin medallas)
complete_counts.fillna(0, inplace=True)

# Guardar los resultados en un archivo CSV
complete_counts.to_csv('athlete_medal_counts_with_no_medals.csv', index=False)

# Imprimir el DataFrame final
print(complete_counts)

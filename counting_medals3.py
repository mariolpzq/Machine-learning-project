import pandas as pd

# Cargar los datos desde el archivo CSV
df = pd.read_csv('olympics_dataset.csv')

# Filtrar las filas donde 'Medal' no sea 'No medal'
df_medals = df[df['Medal'] != 'No medal']

# Eliminar filas duplicadas en función de 'Team', 'Year', 'Sport', 'Event', y 'Medal'
df_unique_medals = df_medals.drop_duplicates(subset=['Team', 'Year', 'Sport', 'Event', 'Medal'])

# Agrupar por 'Team' y 'Year' y contar cada tipo de medalla
medal_counts = df_unique_medals.groupby(['Team', 'Year', 'Medal']).size().unstack(fill_value=0)

# Renombrar las columnas para mayor claridad
medal_counts.columns = ['Bronze', 'Gold', 'Silver']

# Restablecer el índice para que 'Team' y 'Year' sean columnas
medal_counts = medal_counts.reset_index()

# --- Contar el número total de atletas únicos por año ---
# Agrupar por 'Team' y 'Year' y contar los nombres únicos por país y año
athlete_counts = df.groupby(['Team', 'Year'])['Name'].nunique().reset_index()

# Renombrar la columna para que sea clara
athlete_counts.columns = ['Team', 'Year', 'Number of Athletes']

# Unir el DataFrame de medallas con el de conteo de atletas
result = pd.merge(medal_counts, athlete_counts, on=['Team', 'Year'], how='left')

# Reordenar las columnas para incluir el número de atletas al final
result = result[['Team', 'Year', 'Gold', 'Silver', 'Bronze', 'Number of Athletes']]

# Guardar los resultados en un archivo CSV si es necesario
result.to_csv('medal_and_athlete_counts3.csv', index=False)

# Imprimir el DataFrame final
print(result)

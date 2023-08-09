import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('Entel_planes.xlsx')

# Reemplazar los valores en la columna "modalidad"
df['Tipo Oferta'] = df['Tipo Oferta'].map({'Migra': 2, 'Linea Nueva': 1, 'Equipo Libre': 4, 'Renueva': 3})

# Reemplazar los valores en la columna "planes"
df['Plan'] = df['Planes'].map({r'Entel power+ 74.90 R - 20% dto x 3 meses': 43, 
                               r'Entel chip+ 39.90 R': 42, 
                               r'Entel power+ 59.90 R - 20% dto x 3 meses': 46, 
                               r'Entel power 89.90 SD R - 20% dto x 3 meses': 7, 
                               r'Entel Chip 159.90 Plus - 20% dto x 3 meses': 9, 
                               r'Entel power+ 59.90 R': 46, 
                               r'Entel power+ 74.90 R': 43, 
                               r'Entel power 89.90 SD R': 7, 
                               'Entel Chip 159.90 Plus': 9, 
                               'Equipo Libre': 11})

# Guardar el resultado en un nuevo archivo Excel
df.to_excel('nuevo_archivo_entel.xlsx', index=False)

print("DataFrame guardado en el archivo 'nuevo_archivo_entel.xlsx'.")
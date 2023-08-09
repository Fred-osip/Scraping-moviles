import pandas as pd

# Cargamos el archivo Excel
archivo_excel = "Entel_planes.xlsx"  # Reemplaza con la ruta correcta
df = pd.read_excel(archivo_excel)

# Filtramos las filas con "Renueva" en la columna "Plan"
filas_renueva = df[df["Plan"] == "Renueva"]

# Generamos 5 copias de las filas con "Renueva" y las agregamos al DataFrame
nuevas_filas = pd.concat([filas_renueva] * 4, ignore_index=True)

# Concatenamos las nuevas filas al DataFrame original
df = pd.concat([df, nuevas_filas], ignore_index=True)

# Guardamos los cambios en un nuevo archivo Excel
archivo_modificado = "modificador.xlsx"  # Reemplaza con la ruta donde quieres guardar el archivo
df.to_excel(archivo_modificado, index=False)

print("Generación de filas completada y archivo guardado.")
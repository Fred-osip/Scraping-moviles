from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
import time
import timeit #para medir el tiempo de ejecución del código

# Inicia el tiempo de ejecución
inicio = timeit.default_timer()


# URL de la página web
URL = 'https://tienda.bitel.com.pe/partner/products?page='

# Crear instancia del controlador de Selenium
driver = webdriver.Chrome()

# Número de páginas a recorrer
numero_de_paginas = 10

# Lista para almacenar los datos
data = []

j=0
# Iterar sobre las páginas
for i in range(1, numero_de_paginas + 1):
    # Cargar la página
    driver.get(URL + str(i))
    #time.sleep(3)

    # Esperar hasta que un elemento específico se cargue.
    box_items = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "products-list")))

    # Obtener la lista de elementos de productos
    lista_items= box_items.find_elements(By.CLASS_NAME, 'product-item')

    
    # Iterar sobre los elementos de productos
    for item in lista_items:
        j+=1
        print("Scrapeando producto ", j)
        # Obtener los valores del nombre, precio, enlace y disponibilidad.
        #Nombre:
        product_name = item.find_element(By.CLASS_NAME, 'product-brand').text
        
        #Precio
        product_price = item.find_element(By.CLASS_NAME, 'ellipsis-title').text

        #Enlace
        product_link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        #Stock disponible =EXTRAE(D3;18;24)
        product_stock = item.find_element(By.CLASS_NAME, 'mg-t-20').text
        # Sacamos solo el número de "Stock disponible: 105"
        product_stock = int(re.search(r'\d+', product_stock).group()) # Devuelve la primera secuencia de números encontrada

        # Agregar los valores a la lista
        data.append([product_name, product_price, product_link, product_stock])

# Cerrar el navegador
driver.quit()

# Crear un DataFrame de pandas con los datos
df = pd.DataFrame(data, columns=['Nombre', 'Precio', 'Enlace', 'Stock'])

# Guardar el DataFrame en un archivo Excel
df.to_excel('Bitel_liberados_completo.xlsx', index=False)

print("Exportado correctamente en 'Bitel_liberados_completo.xlsx'")


# Eliminamos las filas que tienen stock = 0 
# Filtrar las filas donde el valor en la columna "Disponible" no sea igual a 0
nuevo_df = df[df["Stock"] != 0]

# Exportar el nuevo DataFrame a un archivo excel
nuevo_df.to_excel("Bitel_liberados_disponibles.xlsx", index=False)

print("Exportado correctamente en 'Bitel_liberados_disponibles.xlsx'")


# Finaliza el tiempo de ejecución
fin = timeit.default_timer()

# Calcula la duración en segundos
duracion = fin - inicio

# Imprime el tiempo de ejecución
print("Tiempo de ejecución:", duracion, "segundos")

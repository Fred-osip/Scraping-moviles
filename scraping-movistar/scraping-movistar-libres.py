import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import timeit #para medir el tiempo de ejecución del código

# Inicia el tiempo de ejecución
inicio = timeit.default_timer()



driver = webdriver.Chrome()
base_url = 'https://tienda.movistar.com.pe/celulares/liberados?p={}'

datos = []

for page in range(1, 3):
    url = base_url.format(page)
    driver.get(url)
    time.sleep(3)  # Esperar a que se cargue la página completamente
    
    modelos = driver.find_elements(By.CLASS_NAME, 'hv-equipo')
    
    for i in range(len(modelos)):
        modelo_data = {}
        
        modelos = driver.find_elements(By.CLASS_NAME, 'hv-equipo')
        modelo = modelos[i]
        
        link_element = modelo.find_element(By.TAG_NAME, 'a')
        link = link_element.get_attribute('href')
        modelo_data['link'] = link
        
        modelo.click()
        time.sleep(3)  # Esperar a que se cargue la página
        
        memorias = driver.find_elements(By.CLASS_NAME, 'swatch-attribute-selected-option')
        if len(memorias) > 1:
            modelo_data['Memoria'] = memorias[1].text
        else:
            modelo_data['Memoria'] = ""
        
        nombre_element = driver.find_element(By.CLASS_NAME, 'conteTitleEcoRating')
        modelo_data['Nombre'] = nombre_element.text
        
        btn_contract = driver.find_element(By.CLASS_NAME, 'conteAllbtnTypeContract')
        btn_contract.find_element(By.CLASS_NAME, 'btnTypeContract').click()
        time.sleep(3)  # Esperar a que se cargue la información del contrato
        
        precios = driver.find_elements(By.CLASS_NAME, 'msg-pay-left')
        if len(precios) >= 1:
            precio_texto = precios[0].text
            precio_actual = precio_texto.split('S/')[1].split(' ')[0]  # Obtener solo el primer precio
            modelo_data['Precio'] = 'S/' + precio_actual
        else:
            modelo_data['Precio'] = ""
        
        datos.append(modelo_data)
        
        driver.back()
        time.sleep(2)

driver.quit()

df = pd.DataFrame(datos)
df.to_excel('datos_movistar_v5.xlsx', index=False)
print("Los datos se han exportado correctamente a 'datos_movistar_v4.xlsx'.")

# Finaliza el tiempo de ejecución
fin = timeit.default_timer()

# Calcula la duración en segundos
duracion = fin - inicio

# Imprime el tiempo de ejecución
print("Tiempo de ejecución:", duracion, "segundos")
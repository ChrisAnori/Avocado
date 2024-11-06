'''
-------------------------------
Changelog
-------------------------------
---TOOLKIT v0.1 - 2024-10-29---
AGREGA:
-FUNCION procesar_datos_avocado
-------------------------------
---TOOLKIT v0.2 - 2024-11-02---
AGREGA:
-FUNCION modelos_regresion
-CHANGELOG creado
-------------------------------
---TOOLKIT v0.3 - 2024-11-03---
AGREGA:
-DOCUMENTACION para FUNCION procesar_datos_avocado y modelos_regresion
CORRIGE:
-FUNCION modelos_regresion:
    -No devolvía el tipo correcto dependiendo de la opción, se ajusta la función y se prueba. Ya funciona.
-ERRORES CONOCIDOS:
    -WARNING : mean_squared_error está deprecado -> E:\conda\Lib\site-packages\sklearn\metrics\_regression.py:492: FutureWarning: 'squared' is deprecated in version 1.4 and will be removed in 1.6. To calculate the root mean squared error, use the function'root_mean_squared_error'. 
-------------------------------
---TOOLKIT v0.4 - 2024-11-03---
AGREGA:
-FUNCION formatear_resultados y respectiva DOCUMENTACION
CORRIGE:
-
-ERRORES CONOCIDOS:
    -WARNING : mean_squared_error está deprecado -> E:\conda\Lib\site-packages\sklearn\metrics\_regression.py:492: FutureWarning: 'squared' is deprecated in version 1.4 and will be removed in 1.6. To calculate the root mean squared error, use the function'root_mean_squared_error'. 

uso:
--------------------------------
import sys
import os

# IMPORTANTE - asegurarse de que el path es el correcto, tiene que apuntar a la carpeta Tools (o equivalente si se le cambia el nombre, debería ser Tools)
tools_path = os.path.abspath('./Tools')

# Comprobar si existe la carpeta Tools
if os.path.exists(tools_path):
    sys.path.append(tools_path)
else:
    print("The Tools directory does not exist. Please check the path.")
# importamos toolkit.py
try:
    from toolkit import procesar_datos_avocado  
    from toolkit import regresion_modelos
    from toolkit import formatear_resultados
except ImportError as e:  # Catch ImportError para ver si hay errores al importar
    print(f"ImportError: {e}. comprueba que 'process_dataset' exista en 'toolkit.py'.")
---------------------------------






Parámetros:
filepath - Ruta del archivo CSV donde están los datos
opcion - A o B, indica qué regiones se filtran

Ejemplo de uso:
procesar_datos_avocado('./avocado.csv','B')
'''
La siguiente función recibe un DF, una tabla de Strings y un tipo de modelo y devuelve el R2, RMSE, el intercepto y los coeficientes del mismo
Parámetros:
df - el DataFrame a utilizar
columnas - una tabla con strings, cada string tiene que corresponder al nombre de una columna del DataFrame (df)
Variable_objetivo - la variable objetivo, es decir la 'y' del modelo.
modelo tipo - El tipo de modelo que queremos ajustar, tiene que ser un INT
tipos de modelo:
1 - Lineal
2 - Polinómico(Grado 2 por defecto, se podría añadir otro parámetro para cambiarlo)
3 - Ambos a la vez

La función devuelve un diccionario con los tipos de modelo seleccionados.
Ejemplo de uso:
resultados = regresion_modelos(df, ['Total Volume', 'Total Bags'], 'AveragePrice', modelo_tipo=3)
print(resultados)
TO-DO: funcion que formatee los resultados para que se vea más legible - In progress

'''
'''

'''
función que formatea los resultados de los modelos d una forma más legible --- WIP --- también da una pequeña conclusión dependiendo de los valores de los resultados
PARÁMETROS:
-Resultados ( diccionario resultante con el formato que devuelve la función 'regresión_modelos' )
-Ejemplo de uso:
print(formatear_resultados(resultados))

'''
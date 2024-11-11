# Análisis del Mercado de Aguacate

Este documento proporciona un análisis detallado sobre las tendencias de precios y ventas del mercado de aguacates en Estados Unidos desde 2015 hasta 2018.

---

## 1. Tendencias Generales de Precios y Ventas

### 1.1 Observaciones de Estacionalidad
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/1_1.png" alt="Gráfico de resultados" width="500"/>    

Observamos una **tendencia estacional** en el consumo de aguacates, influenciada tanto por la **producción** como por la **demanda** en meses más calurosos. 

#### Incremento de Precios en 2016
- **Popularidad**: En 2016, la popularidad del aguacate aumentó, impulsando el precio debido a una mayor demanda.
- **Problemas de Suministro**: Posibles problemas climáticos en México y California afectaron la oferta, elevando los precios.

#### Escasez de Oferta en 2017
- La producción disminuyó debido a **condiciones climáticas adversas en México**, aumentando los precios en EE.UU.
- La **variabilidad mensual** en ventas es notable, con fluctuaciones debido a temporadas altas y bajas de consumo.

### 1.2 Cambios en el Precio Promedio
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/1_2.png" alt="Gráfico de resultados" width="500"/> 
Se observa que los cambios de precio son más bruscos en las **épocas de mayor y menor producción**, así como en los meses más calurosos.

## 1.3 
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/1_3.png" alt="Gráfico de resultados" width="500"/> 
También observamos inicialmente una fuerte relación entre la estacionalidad y el volumen de ventas. Sería útil modificar los periodos a estudiar en los modelos de regresión para incluir esta variable si aún no está en el ejercicio, así como **segmentar los meses que sospechamos pueden influir más en el aumento del consumo**, como los meses entre junio y septiembre, debido al periodo estival y la época de recolección del aguacate.

## 1.4
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/1_4.png" alt="Gráfico de resultados" width="500"/> 
**Picos de Ventas ** 
Cada año, en el **mes de febrero se alcanza un pico máximo de ventas de aguacates**. Después de este punto, las ventas tienden a disminuir durante los siguientes cinco meses, hasta alcanzar un valor cercano al máximo nuevamente en el quinto mes. Esta recurrencia sugiere un evento específico que impulsa el consumo de aguacates en febrero.

Una hipótesis probable es que este **aumento en ventas esté relacionado con el evento del Super Bowl en Estados Unidos**, donde el consumo de guacamole, y por ende de aguacates, aumenta significativamente.

**Valles de Ventas**  
Los peores resultados en ventas se concentran en los **últimos tres meses de cada año**. Estos "valles" en el volumen total de ventas se repiten consistentemente en este periodo, posiblemente debido a una reducción en la demanda o a la finalización de la temporada de cosecha del aguacate, lo cual afecta la oferta en el mercado.

**Estacionalidad en los Datos**  
Dado que tanto los picos como los valles de ventas se presentan en los mismos periodos año tras año, podemos afirmar que existe una estacionalidad en los datos. Ejemplos específicos incluyen:

- **Meses de verano**: Se percibe una tendencia al alza en las ventas, aunque sin alcanzar el pico máximo de febrero.
- **Septiembre a Diciembre**: Este periodo muestra consistentemente los valores de ventas más bajos en cada año, probablemente debido a una reducción en la demanda y el fin de la cosecha.

## 1.5
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/1_5.png" alt="Gráfico de resultados" width="500"/> 
Los datos de cambios en el precio promedio anual indican que en 2015, 2016 y 2018 se mantuvo una tendencia en el rango de precios entre $1.34 y $1.30. Sin embargo, en **2017 se registra un incremento significativo, alcanzando $1.47**. Podrían buscarse factores ambientales, como desastres que afectaran la producción, políticas sobre precios o aranceles en productos importados, dado que México es un gran productor de aguacates y no forma parte de los Estados Unidos. 

Además, puede considerarse la influencia de eventos o promociones que involucren el aguacate, como la aparición de una figura pública que popularizara su consumo en EE.UU. Este análisis ayuda a visualizar y entender factores que pueden afectar los precios en productos agrícolas, y brinda una oportunidad para practicar técnicas básicas de visualización y sacar conclusiones simples sobre datos de consumo.


---

## 2. Análisis por Región

### 2.1 Comparación de Volúmenes de Venta
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/2_1.png" alt="Gráfico de resultados" width="500"/> 
- **California**: Volumen de ventas más alto y con alta variabilidad.
- **Plains**: Menor rango de ventas, con ventas bajas y consistentes.
- En **California y West**, se observan valores atípicos, posiblemente relacionados con **eventos de alta demanda**.

### 2.2 Cambios de Precio Promedio (2015-2017)
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/2_2.png" alt="Gráfico de resultados" width="500"/> 
El precio promedio anual muestra variabilidad debido a factores externos, como el clima y la política comercial entre EE.UU. y México.

- **2015**: Baja variabilidad y estabilidad en precios.
- **2016**: Aumento en la dispersión de precios.
- **2017**: Alta variabilidad y un aumento significativo de precios debido a fenómenos climáticos y eventos de demanda masiva.

### 2.3 Rango Principal de Ventas
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/2_3.png" alt="Gráfico de resultados" width="500"/> 
El mayor rango de ventas se observa entre **28,000 y 34,000 unidades**.

### 2.4 Análisis por Tipo de Bolsa
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/2_4.png" alt="Gráfico de resultados" width="500"/> 
La mayor parte del volumen de ventas corresponde a **Small Bags**, seguido de **Large Bags**. Las **XLarge Bags** representan un porcentaje menor.

---

## 3. Análisis de Elasticidad Precio-Demanda

### 3.1 Interpretación de Elasticidad
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/3_1.png" alt="Gráfico de resultados" width="500"/> 
La elasticidad precio-demanda es negativa en todo el período, con valores que varían entre **-2.1 y -1**. Este comportamiento sugiere una **demanda elástica** donde un aumento en el precio genera una disminución en la cantidad demandada.

#### Análisis por Año
- **2015-2016**: Estabilidad en la elasticidad y la demanda.
- **2017**: Elasticidad cercana a -1.2, posiblemente debido a la "fiebre del aguacate" y un aumento de la demanda internacional.

### 3.2 Factores de Elasticidad en South Central
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/3_2.png" alt="Gráfico de resultados" width="500"/> 
La elasticidad en esta región es negativa y relativamente baja debido a factores como:
- **Proximidad a México**
- **Poder adquisitivo** de las áreas metropolitanas
- **Alta preferencia** por el aguacate como alimento esencial en la dieta local.

### 3.3 Elasticidad por Tipo de Bolsa
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/3_3.png" alt="Gráfico de resultados" width="500"/>
La elasticidad negativa en **Small Bags** y **Large Bags** indica que el precio y la demanda se comportan de forma inversa.

### 3.4 Elasticidad por Tipo de Aguacate
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/3_4.png" alt="Gráfico de resultados" width="500"/>
Tanto los aguacates **convencionales** como los **orgánicos** presentan una elasticidad negativa, lo cual refleja que los cambios en precio afectan fuertemente la demanda.

---

## 4. Estacionalidad y Eventos Clave

### 4.1 Relación Precio-Volumen de Ventas
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_1.png" alt="Gráfico de resultados" width="500"/>
La relación entre **precio y volumen** de ventas muestra una elasticidad negativa, con ventas que aumentan drásticamente en febrero, probablemente por el evento de la **Super Bowl**.
![Gráfico de Evolución Precios Promedio y Volmen Total de Ventas con Regiones de la SuperBowl](img_avo/4_1_2.jpg)
![Gráfico de Evolución Precio Promedio en Regiones de la SperBowl](img_avo/4_1_3.jpg)


### 4.2 Relación Geográfica y Precios
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_2.png" alt="Gráfico de resultados" width="500"/>
Las regiones del **Sur y Oeste de EE.UU.** presentan precios más altos, lo cual podría estar relacionado con su proximidad a México.

### 4.3 Diferencias en Volúmenes de Venta por Tipo de Bolsa
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_3.png" alt="Gráfico de resultados" width="500"/>
El comportamiento de ventas de **Small Bags** y **Large Bags** refleja una estacionalidad notable, con picos de ventas en febrero y mayor estabilidad en otros periodos.

### 4.4 Diferencias en Volúmenes de Venta por Tipo de Bolsa
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_4.png" alt="Gráfico de resultados" width="500"/>
El comportamiento de ventas de **Small Bags** y **Large Bags** refleja 

### 4.5 Diferencias en Volúmenes de Venta por Tipo de Bolsa
<img src="img_avo/4_5.png" alt="Gráfico de resultados" width="500"/>
El comportamiento de ventas de **Small Bags** y **Large Bags** refleja 
---

## Conclusiones
El análisis del mercado de aguacates muestra una clara **estacionalidad** y una **alta sensibilidad de la demanda al precio**, influenciada por factores climáticos, socioeconómicos y culturales en Estados Unidos.

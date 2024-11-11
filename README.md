# Análisis del Mercado de Aguacate

Este documento proporciona un análisis detallado sobre las tendencias de precios y ventas del mercado de aguacates en Estados Unidos desde 2015 hasta 2018.
El obejtivo de este Proyecto es encontrar los mejores modelos que sean capaces de predecir los precios y ventas de aguacates en el futuro.
---

# Introducción

## Reglas de Trabajo

1. Trabajar cada persona en su branch correspondiente.
2. Push dentro de la rama de cada persona.
3. Asignación de las tareas a realizar previa al comienzo de cada ejercicio. Control en TRELLO organizado por semanas y personas.
4. Reunión diaria 30 minutos antes de clase para comunicar incidencias, dudas o avances realizados.
5. Mantenerse activos en los canales de comunicación del grupo (Discord, Whatsapp) y avisar en caso de no poder acudir.


## Planificación

Hemos realizado la planificación a diario con Trello para organizar las tareas y mantenernos en contacto. A continuación, se muestra el gráfico de resultados de la planificación realizada:

<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/trello.png" alt="Gráfico de resultados" width="500"/>

Así como se ha mantenido el control y nueva asignación de tareas con los Daily Meetings.

## Toolkit

Hemos creado un TOOLKIT para poder realizar el análisis de datos de manera más eficiente y rápida.
Dentro de Toolkit existe el README donde indicamos el funcionamiento.

---

## Investigación posibles factores externos que puedan afectar a los datos:

# 2017 Septiembre : Huracán Irma
https://www.latimes.com/espanol/eeuu/articulo/2017-09-14/efe-3379551-13366931-20170914


# Respuesta de Trump a Mexico en Febrero subiendo los impuestos a productos de Mexico
https://www.elmundo.es/internacional/2017/01/26/588a0b0f22601da9468b45b8.html


# Consumo masivo de Aguacate en la SUPERBOWL
https://www.visionfruticola.com/2023/07/el-aguacate-en-el-super-bowl-y-como-se-convirtio-en-el-jugador-mas-valioso-de-la-mesa/



## 1. Tendencias Generales de Precios y Ventas

### 1.1 Observaciones de Estacionalidad --------
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/1_1.png" alt="Gráfico de resultados" width="500"/>    

Observamos una tendencia estacional en el consumo de aguacates, influenciada tanto por la producción como por la demanda en meses más calurosos. 

#### Incremento de Precios en 2016
- Popularidad: En 2016, la popularidad del aguacate aumentó, impulsando el precio debido a una mayor demanda.
- Problemas de Suministro: Posibles problemas climáticos en México y California afectaron la oferta, elevando los precios.

#### Escasez de Oferta en 2017
- La producción disminuyó debido a condiciones climáticas adversas en México, aumentando los precios en EE.UU.
- La variabilidad mensual en ventas es notable, con fluctuaciones debido a temporadas altas y bajas de consumo.

## 1.3 Promedio precios de Aguacate por Meses
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/1_3.png" alt="Gráfico de resultados" width="500"/> 
También observamos inicialmente una fuerte relación entre la estacionalidad y el volumen de ventas. Sería útil modificar los periodos a estudiar en los modelos de regresión para incluir esta variable si aún no está en el ejercicio, así como **segmentar los meses que sospechamos pueden influir más en el aumento del consumo**, como los meses entre junio y septiembre, debido al periodo estival y la época de recolección del aguacate.

## 1.4 Ventas de Aguacate a lo largo del tiempo
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/1_4.png" alt="Gráfico de resultados" width="500"/> 

**Pico de Ventas** 
Cada año, en el mes de febrero se alcanza un pico máximo de ventas de aguacates. Después de este punto, las ventas tienden a disminuir durante los siguientes cinco meses, hasta alcanzar un valor cercano al máximo nuevamente en el quinto mes. Esta recurrencia sugiere un evento específico que impulsa el consumo de aguacates en febrero.

Una hipótesis probable es que este aumento en ventas esté relacionado con el evento del Super Bowl en Estados Unidos, donde el consumo de guacamole, y por ende de aguacates, aumenta significativamente.

**Valles de Ventas** 
Los peores resultados en ventas se concentran en los últimos tres meses de cada año. Estos "valles" en el volumen total de ventas se repiten consistentemente en este periodo, posiblemente debido a una reducción en la demanda o a la finalización de la temporada de cosecha del aguacate, lo cual afecta la oferta en el mercado.

**Estacionalidad en los Datos**
Dado que tanto los picos como los valles de ventas se presentan en los mismos periodos año tras año, podemos afirmar que existe una estacionalidad en los datos. Ejemplos específicos incluyen:

- **Meses de verano**: Se percibe una tendencia al alza en las ventas, aunque sin alcanzar el pico máximo de febrero.
- **Septiembre a Diciembre**: Este periodo muestra consistentemente los valores de ventas más bajos en cada año, probablemente debido a una reducción en la demanda y el fin de la cosecha.

## 1.5 Cambios Precio Promedio anuales
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_5.png" alt="Gráfico de resultados" width="500"/> 
Los datos de cambios en el precio promedio anual indican que en 2015, 2016 y 2018 se mantuvo una tendencia en el rango de precios entre $1.34 y $1.30. Sin embargo, en 2017 se registra un incremento significativo, alcanzando $1.47. Podrían buscarse factores ambientales, como desastres que afectaran la producción, políticas sobre precios o aranceles en productos importados, dado que México es un gran productor de aguacates y no forma parte de los Estados Unidos. 

Además, puede considerarse la influencia de eventos o promociones que involucren el aguacate, como la aparición de una figura pública que popularizara su consumo en EE.UU. Este análisis ayuda a visualizar y entender factores que pueden afectar los precios en productos agrícolas, y brinda una oportunidad para practicar técnicas básicas de visualización y sacar conclusiones simples sobre datos de consumo.

---

## 2. Análisis por Región

### 2.1 Comparación de Volúmenes de Venta
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/2_1.png" alt="Gráfico de resultados" width="500"/>

**California**
Volumen de ventas más alto y con alta variabilidad.

- **Plains**
Menor rango de ventas, con ventas bajas y consistentes.

- **California y West**
Se observan valores atípicos, posiblemente relacionados con **eventos de alta demanda**.

### 2.2 Cambios de Precio Promedio (2015-2017)
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/2.2.png" alt="Gráfico de resultados" width="500"/> 
El precio promedio anual muestra variabilidad debido a factores externos, como el clima y la política comercial entre EE.UU. y México.

- **2015**: Baja variabilidad y estabilidad en precios.
- **2016**: Aumento en la dispersión de precios.
- **2017**: Alta variabilidad y un aumento significativo de precios debido a fenómenos climáticos y eventos de demanda masiva.

---

## 3. Análisis de Elasticidad Precio-Demanda

### 3.1 Interpretación de Elasticidad
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/3_1.png" alt="Gráfico de resultados" width="500"/> 
La elasticidad precio-demanda es negativa en todo el período, con valores que varían entre -2.1 y -1. Este comportamiento sugiere una **demanda elástica donde un aumento en el precio genera una disminución en la cantidad demandada.

#### Análisis por Año
- **2015-2016**: Estabilidad en la elasticidad y la demanda.
- **2017**: Elasticidad cercana a -1.2, posiblemente debido a la "fiebre del aguacate" y un aumento de la demanda internacional.

### 3.2 Factores de Elasticidad en South Central (añadir comentarios)
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/3_2.png" alt="Gráfico de resultados" width="500"/> 
La elasticidad en esta región es negativa y relativamente baja debido a factores como:

**Proximidad a México**
**Poder adquisitivo** de las áreas metropolitanas
**Alta preferencia** por el aguacate como alimento esencial en la dieta local.

### 3.3 Elasticidad por Tipo de Bolsa
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/3_3.png" alt="Gráfico de resultados" width="500"/>
La elasticidad negativa en **Small Bags** y **Large Bags** indica que el precio y la demanda se comportan de forma inversa.

---

## 4. Estacionalidad y Eventos Clave

### 4.1 Relación Precio-Volumen de Ventas
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_1_1.png" alt="Gráfico de resultados" width="500"/>
La relación entre precio y volumen de ventas muestra una elasticidad negativa, con ventas que aumentan drásticamente en febrero, probablemente por el evento de la Super Bowl.


<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_1_2.png" alt="Gráfico de resultados" width="500"/>
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_1_3.png" alt="Gráfico de resultados" width="500"/>


### 4.3 Diferencias en Ventas total por Tipo de Bolsa
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_3.png" alt="Gráfico de resultados" width="500"/>
El comportamiento de ventas de Small Bags y Large Bags refleja una estacionalidad notable, con picos de ventas en febrero y mayor estabilidad en otros periodos.

Se contemplan las variaciones en las preferencias de consumidor 

### 4.4 Diferencias en Volúmenes de Venta por Tipo de Bolsa
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/4_4.png" alt="Gráfico de resultados" width="500"/>
El comportamiento de ventas demuestra qe no importa que tipo de consumidor sea a la hora del volumen que consume ya que en todos los casos se comporta igual.

### 4.5 Retención de Ventas por Mes desde la Primera Venta
<img src="img_avo/4_5.png" alt="Gráfico de resultados" width="500"/>

---

## 5. Análisis de Correlación y Regresión

### 5.1 Relación Precio-Volumen de Ventas
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_1_1.png" alt="Gráfico de resultados" width="500"/>
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_1_2.png" alt="Gráfico de resultados" width="500"/>
Viendo el mapa de calor, vemos las siguientes correlaciones altas:

-Total Volume y Total Bags con 0.9
-Total Volume con 4046 0.87
-Total Volume con 4225 0.83

Esto sugiere que puede haber una fuerte relación lineal entre esos campos.

### 5.2 Análisis de Dispersión entre Variables Clave
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_2.png" alt="Gráfico de resultados" width="500"/>
Regresión Lineal (color verde): Representa una tendencia lineal que muestra la relación directa y general entre Total Volume y AveragePrice. 

Si la pendiente es negativa, sugiere que un mayor volumen total de ventas está asociado con precios más bajos (indicación de que un exceso de oferta reduce el precio). Curva Polinómica: A partir del 0.6 y 0.8 de volumen reduce la sensibilidad a cambios de precios.

### 5.3 Predicciones Mensuales Usando Datos Trimestrales
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_3.png" alt="Gráfico de resultados" width="500"/>
Se ve que el modelo se ajusta muy bien, excepto el trimestre 1 del 2016 , que puede ser debido por el hecho del evento detectado de la SUPERBOWL , el cual genera una expectativa dentro del mercado que el modelo no es capaz de predecir

### 5.4 Predicciones Trimestral
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_4.png" alt="Gráfico de resultados" width="500"/>

Modelo de Regresión Lineal - R^2: 1.0, RMSE: 2.1259152388627147e-16
Modelo de Regresión Polinómica - R^2: 1.0, RMSE: 1.5700924586837752e-16
Modelo Ridge - R^2: 1.0, RMSE: 1.5594575338023796e-11

Pequeño tamaño de datos: puede que no haya suficientes puntos de entrenamiento para que los modelos generalicen correctamente.

Características demasiado predictivas: Si los datos son muy lineales o tienen una relación muy clara entre las características (como en el caso de datos económicos trimestrales), los modelos lineales (y especialmente Ridge) pueden ajustarse de manera casi perfecta.

Regularización en Ridge: Aunque el modelo Ridge utiliza regularización, en casos de sobreajuste, esto puede no ser suficiente,dependiendo de los datos.

### 5.5 Predicciones Trimestral
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_5.png" alt="Gráfico de resultados" width="500"/>
Modelo Lineal - R^2: -2.06982131101471, RMSE: 0.12909294762093804
Modelo Polinómico - R^2: -2.06982131101471, RMSE: 0.12909294762093804

Observamos la confirmación de una de las hipotesis 2017 

### 5.7 Análisis de Coeficientes de Regresión Múltiple
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_7.png" alt="Gráfico de resultados" width="500"/>

Explorar un modelo más complejo: Tal vez probar con modelos no lineales o más complejos (como árboles de decisión, Random Forest, o incluso redes neuronales) si el conjunto de datos es suficientemente grande.

### 5.8 Modelos de Regresión para Diferenciar Volúmenes de Ventas:
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_8.png" alt="Gráfico de resultados" width="500"/>

Explorar un modelo más complejo: Tal vez probar con modelos no lineales o más complejos (como árboles de decisión, Random Forest, o incluso redes neuronales) si el conjunto de datos es suficientemente grande.

### 5.9 Análisis de la Influencia de las Ventas Totales en el Precio Promedio:
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_9.png" alt="Gráfico de resultados" width="500"/>

Explorar un modelo más complejo: Tal vez probar con modelos no lineales o más complejos (como árboles de decisión, Random Forest, o incluso redes neuronales) si el conjunto de datos es suficientemente grande.

### 5.10 Regresión para Predecir el Precio Promedio Según el Volumen de Aguacates por Tipo:
<img src="https://github.com/largouuuxyz/Avocado/blob/cristian/images/5_10.png" alt="Gráfico de resultados" width="500"/>

Explorar un modelo más complejo: Tal vez probar con modelos no lineales o más complejos (como árboles de decisión, Random Forest, o incluso redes neuronales) si el conjunto de datos es suficientemente grande.

## Conclusiones
El análisis del mercado de aguacates muestra una clara **estacionalidad** y una **alta sensibilidad de la demanda al precio**, influenciada por factores climáticos, socioeconómicos y culturales en Estados Unidos.

Los modelos que hemos utilizado se quedan algo simples a la hora de poder Predecir a futuro, ya que no son capaces de comprender factores externos a la base de datos en momentos puntuales que son ciertamente aleatorios.

Seguramente aplicando nuevos métodos y nuevas técnicas mas avanzadas del Curso podriamos lograr unos mejores resultados.

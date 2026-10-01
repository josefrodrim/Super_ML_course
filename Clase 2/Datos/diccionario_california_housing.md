# Diccionario de datos · California Housing

**Curso:** Machine Learning · Programa de Especialización Data Scientist · Clase 2
**Docente:** Josef Renato Rodriguez
**Archivo:** `california_housing.csv` · 20 640 filas · 10 columnas · separador coma · con encabezado

---

## 1. Qué es

Cada fila es un **block group** del censo de Estados Unidos de 1990 en el estado de California. Un block group es la unidad geográfica más pequeña para la que la Oficina del Censo publica datos de muestra; suele tener entre 600 y 3 000 habitantes. En el curso los llamamos **distritos**.

Todas las columnas describen el distrito completo, no una vivienda individual: son totales (habitaciones, población) o medianas (ingreso, antigüedad, valor).

**Variable objetivo:** `median_house_value`, el valor mediano de las viviendas del distrito.

## 2. Fuente

| | |
|---|---|
| Datos originales | Pace, R. K. y Barry, R. (1997). Sparse spatial autoregressions. *Statistics & Probability Letters*, 33(3), 291–297. Construido con el censo de California de 1990. |
| Versión usada | La del repositorio del libro *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow* (Aurélien Géron): `github.com/ageron/handson-ml2`, carpeta `datasets/housing`. |
| Diferencias con el original | Según el propio repositorio: (1) se borraron al azar 207 valores de `total_bedrooms`, para practicar el tratamiento de faltantes; (2) se añadió la columna categórica `ocean_proximity`. |

## 3. Columnas

| # | Columna | Tipo | Unidad | Descripción | Mín | Mediana | Máx | Faltantes |
|---|---|---|---|---|---|---|---|---|
| 1 | `longitude` | numérica continua | grados | Longitud del centro del distrito. Más negativa = más al oeste (hacia el Pacífico). | −124.35 | −118.49 | −114.31 | 0 |
| 2 | `latitude` | numérica continua | grados | Latitud del centro del distrito. Mayor = más al norte. | 32.54 | 34.26 | 41.95 | 0 |
| 3 | `housing_median_age` | numérica | años | Antigüedad mediana de las viviendas del distrito. **Topada en 52.** | 1 | 29 | 52 | 0 |
| 4 | `total_rooms` | numérica discreta | habitaciones | Total de habitaciones de todas las viviendas del distrito. | 2 | 2 127 | 39 320 | 0 |
| 5 | `total_bedrooms` | numérica discreta | dormitorios | Total de dormitorios de todas las viviendas del distrito. | 1 | 435 | 6 445 | **207** |
| 6 | `population` | numérica discreta | personas | Habitantes del distrito. | 3 | 1 166 | 35 682 | 0 |
| 7 | `households` | numérica discreta | hogares | Número de hogares del distrito. | 1 | 409 | 6 082 | 0 |
| 8 | `median_income` | numérica continua | decenas de miles de USD al año | Ingreso mediano de los hogares. 3.5 equivale a unos 35 000 USD. **Topado en 15.0001 y con piso en 0.4999.** | 0.4999 | 3.5348 | 15.0001 | 0 |
| 9 | `median_house_value` | numérica continua | USD | **Variable objetivo.** Valor mediano de las viviendas del distrito. **Topado en 500 001.** | 14 999 | 179 700 | 500 001 | 0 |
| 10 | `ocean_proximity` | categórica nominal | — | Cercanía aproximada al océano. Ver tabla de categorías. | — | — | — | 0 |

### Categorías de `ocean_proximity`

| Valor | Significado | Distritos | % |
|---|---|---|---|
| `<1H OCEAN` | a menos de una hora del océano | 9 136 | 44.3 % |
| `INLAND` | tierra adentro | 6 551 | 31.7 % |
| `NEAR OCEAN` | cerca del océano | 2 658 | 12.9 % |
| `NEAR BAY` | cerca de la bahía de San Francisco | 2 290 | 11.1 % |
| `ISLAND` | en una isla | 5 | 0.02 % |

En la Clase 2, `get_dummies(..., drop_first=True)` elimina `<1H OCEAN` (es la primera en orden alfabético), que queda como **categoría de referencia**.

## 4. Advertencias de calidad

Estas características son parte del dataset real y se trabajan a propósito en la clase.

| Tema | Detalle | Cómo se trata en la Clase 2 |
|---|---|---|
| **Valores topados en el objetivo** | 965 distritos (4.7 %) tienen `median_house_value` = 500 001. Su valor real era mayor, pero el censo no lo registró. | Se identifican en el gráfico de residuos (forman una diagonal) y se mide cuánto pesan en el MAE y el RMSE. |
| **Topes en variables explicativas** | `housing_median_age` = 52 en 1 273 distritos. `median_income` = 15.0001 en 49. | Se mencionan; no se corrigen. |
| **Datos faltantes** | 207 vacíos en `total_bedrooms` (1.0 %). | Se rellenan con la mediana **calculada solo con el entrenamiento**. |
| **Categoría casi vacía** | `ISLAND` tiene 5 distritos. | El corte train/test se estratifica por `ocean_proximity`. Su coeficiente no se interpreta. |
| **Multicolinealidad** | `total_rooms`, `total_bedrooms`, `population` y `households` miden casi lo mismo: el tamaño del distrito. VIF entre 6 y 30. | Se mide con el VIF y se muestra un arreglo con razones por hogar. |
| **Unidad de observación** | Son distritos, no viviendas. `total_rooms` no es el número de habitaciones de una casa. | Para hablar de una vivienda típica se construyen razones: habitaciones por hogar, dormitorios por habitación, personas por hogar. |
| **Antigüedad de los datos** | Precios de 1990, sin ajustar por inflación. | El dataset se usa para aprender el método, no para tasar viviendas actuales. |

## 5. Variables derivadas usadas en la clase

| Variable | Fórmula | Qué representa |
|---|---|---|
| `cuartos_por_hogar` | `total_rooms / households` | tamaño de la vivienda típica |
| `dormitorios_por_cuarto` | `total_bedrooms / total_rooms` | qué parte de la vivienda son dormitorios |
| `personas_por_hogar` | `population / households` | cuántas personas viven en cada hogar |

## 6. Cómo cargarlo

```python
import pandas as pd

URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
try:
    casas = pd.read_csv(URL)
except Exception:
    casas = pd.read_csv("california_housing.csv")   # subido a Colab o al repo del curso
```

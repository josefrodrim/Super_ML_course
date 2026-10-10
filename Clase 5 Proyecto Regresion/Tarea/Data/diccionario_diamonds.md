# Diccionario de datos · Diamonds

**Curso:** Machine Learning · Programa de Especialización Data Scientist · Tarea de la Clase 5
**Docente:** Josef Renato Rodriguez
**Archivo:** `diamonds.csv` · 53 940 filas · 10 columnas · separador coma · con encabezado

---

## 1. Qué es

Cada fila es **un diamante de talla redonda** con su precio y sus atributos de calidad y tamaño. La variable objetivo es `price`.

## 2. Fuente

| | |
|---|---|
| Datos originales | Dataset `diamonds` del paquete ggplot2 de R: Wickham, H. (2016). *ggplot2: Elegant Graphics for Data Analysis*. Springer. |
| Archivo usado | Copia publicada en `github.com/mwaskom/seaborn-data` (`diamonds.csv`). |

## 3. Columnas

| # | Columna | Tipo | Unidad | Descripción | Mín | Mediana | Máx | Faltantes |
|---|---|---|---|---|---|---|---|---|
| 1 | `carat` | numérica | quilates | Peso del diamante. 1 quilate = 0.2 gramos. | 0.2 | 0.7 | 5.01 | 0 |
| 2 | `cut` | ordinal | — | Calidad de la talla, de peor a mejor: Fair < Good < Very Good < Premium < Ideal. | — | — | — | 0 |
| 3 | `color` | ordinal | — | Color, de peor a mejor: J < I < H < G < F < E < D. **D es el mejor** (el más incoloro). | — | — | — | 0 |
| 4 | `clarity` | ordinal | — | Pureza (inclusiones), de peor a mejor: I1 < SI2 < SI1 < VS2 < VS1 < VVS2 < VVS1 < IF (sin inclusiones internas). | — | — | — | 0 |
| 5 | `depth` | numérica | % | Profundidad total como porcentaje del ancho promedio: z / promedio(x, y) × 100. | 43 | 61.8 | 79 | 0 |
| 6 | `table` | numérica | % | Ancho de la cara superior (la «mesa») como porcentaje del punto más ancho. | 43 | 57 | 95 | 0 |
| 7 | `price` | numérica | USD | **Variable objetivo.** Precio del diamante. | 326 | 2 401 | 18 823 | 0 |
| 8 | `x` | numérica | mm | Largo. | 0 | 5.7 | 10.74 | 0 |
| 9 | `y` | numérica | mm | Ancho. | 0 | 5.71 | 58.9 | 0 |
| 10 | `z` | numérica | mm | Profundidad (alto). | 0 | 3.53 | 31.8 | 0 |

## 4. Para tener en cuenta

- Las medidas `x`, `y` y `z` de un diamante real no pueden ser cero, y ningún diamante de este rango de peso mide varios centímetros.
- `cut`, `color` y `clarity` tienen un orden natural. Respétalo al codificarlas.

# Diccionario de datos · Ames Housing

**Curso:** Machine Learning · Programa de Especialización Data Scientist · Clase 5
**Docente:** Josef Renato Rodriguez
**Archivo:** `ames_housing.csv` · 2 930 filas · 24 columnas · separador coma · con encabezado

---

## 1. Qué es

Cada fila es **una venta de una vivienda** en Ames, Iowa (Estados Unidos), registrada por la oficina de tasación de la ciudad entre 2006 y 2010. La variable objetivo es `sale_price`. Las superficies están en pies cuadrados (1 pie² = 0.093 m²).

## 2. Fuente

| | |
|---|---|
| Datos originales | De Cock, D. (2011). Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. *Journal of Statistics Education*, 19(3). |
| Archivo usado | Copia del archivo original de 2 930 ventas y 82 columnas, publicada en `github.com/wblakecannon/ames` (`data/housing.csv`). |
| Selección | Para la clase se conservan 22 variables, el identificador y el precio, con nombres en minúsculas y guion bajo. |
| Recomendación del autor | De Cock recomienda excluir las viviendas de más de 4 000 pies² de superficie habitable (5 casos: tres ventas parciales que no reflejan el valor de mercado y dos casas muy grandes con precios acordes a su tamaño). |

## 3. Columnas

| # | Columna | Tipo | Unidad | Descripción | Mín | Mediana | Máx | Faltantes |
|---|---|---|---|---|---|---|---|---|
| 1 | `pid` | identificador | — | Número de parcela de la propiedad. Una fila por venta. | — | — | — | 0 |
| 2 | `sale_price` | numérica | USD | **Variable objetivo.** Precio de venta. | 12 789 | 160 000 | 755 000 | 0 |
| 3 | `gr_liv_area` | numérica | pies² | Superficie habitable sobre el nivel del suelo (no incluye sótano). 1 pie² = 0.093 m². | 334 | 1 442 | 5 642 | 0 |
| 4 | `total_bsmt_sf` | numérica | pies² | Superficie total del sótano. 0 si no tiene. | 0 | 990 | 6 110 | 1 |
| 5 | `lot_area` | numérica | pies² | Superficie del lote (terreno). | 1 300 | 9 436 | 215 245 | 0 |
| 6 | `lot_frontage` | numérica | pies | Longitud de calle frente al lote, en pies lineales. Faltante = no se registró. | 21 | 68 | 313 | 490 |
| 7 | `year_built` | numérica | año | Año de construcción. | 1872 | 1973 | 2010 | 0 |
| 8 | `year_remod` | numérica | año | Año de la última remodelación o ampliación (igual al de construcción si nunca se remodeló). | 1950 | 1993 | 2010 | 0 |
| 9 | `overall_qual` | ordinal 1–10 | puntaje | Calidad general del material y la terminación, asignada por el tasador. 1 = muy pobre, 10 = excelente. | 1 | 6 | 10 | 0 |
| 10 | `overall_cond` | ordinal 1–10 | puntaje | Estado general de conservación. 1 = muy pobre, 10 = excelente. | 1 | 5 | 9 | 0 |
| 11 | `garage_cars` | numérica | autos | Capacidad del garaje, en número de autos. | 0 | 2 | 5 | 1 |
| 12 | `garage_type` | categórica | — | Ubicación del garaje: Attchd (adosado), Detchd (separado), BuiltIn (integrado), Basment (en el sótano), 2Types (más de un tipo), CarPort (cochera abierta). **Faltante = no tiene garaje.** | — | — | — | 157 |
| 13 | `full_bath` | numérica | baños | Baños completos sobre el nivel del suelo. | 0 | 2 | 4 | 0 |
| 14 | `half_bath` | numérica | baños | Medios baños (sin ducha) sobre el nivel del suelo. | 0 | 0 | 2 | 0 |
| 15 | `bedrooms` | numérica | dormitorios | Dormitorios sobre el nivel del suelo (no cuenta los del sótano). | 0 | 3 | 8 | 0 |
| 16 | `fireplaces` | numérica | chimeneas | Número de chimeneas. | 0 | 1 | 4 | 0 |
| 17 | `mas_vnr_area` | numérica | pies² | Superficie de enchapado de mampostería (ladrillo o piedra) en la fachada. | 0 | 0 | 1 600 | 23 |
| 18 | `neighborhood` | categórica | — | Barrio dentro de los límites de la ciudad de Ames (28 códigos, por ejemplo StoneBr, NoRidge, MeadowV). | — | — | — | 0 |
| 19 | `kitchen_qual` | ordinal | — | Calidad de la cocina: Ex (excelente) > Gd (buena) > TA (típica) > Fa (regular) > Po (pobre). | — | — | — | 0 |
| 20 | `central_air` | categórica | — | Aire acondicionado central: Y (sí), N (no). | — | — | — | 0 |
| 21 | `bsmt_qual` | ordinal | — | Altura del sótano: Ex (100+ pulgadas), Gd (90–99), TA (80–89), Fa (70–79), Po (< 70). **Faltante = no tiene sótano.** | — | — | — | 80 |
| 22 | `sale_condition` | categórica | — | Condición de la venta: Normal; Abnorml (venta forzada: remate, ejecución); AdjLand (compra de terreno vecino); Alloca (dos propiedades con escrituras separadas); Family (entre familiares); Partial (casa nueva no terminada al momento de la tasación). | — | — | — | 0 |
| 23 | `ms_zoning` | categórica | — | Zonificación: RL (residencial baja densidad), RM (media), RH (alta), FV (residencial de villa flotante), C (all) (comercial), I (all) (industrial), A (agr) (agrícola). | — | — | — | 0 |
| 24 | `yr_sold` | numérica | año | Año de la venta (2006 a 2010). | 2006 | 2008 | 2010 | 0 |

## 4. Advertencias

- **Dos tipos de faltantes.** En `garage_type` y `bsmt_qual`, el faltante significa «no tiene». En `lot_frontage`, `mas_vnr_area`, `total_bsmt_sf` y `garage_cars` significa «no se registró».
- **Precio asimétrico.** Mediana 160 000 USD, máximo 755 000. Conviene modelar `log(sale_price)`.
- **Ventas parciales.** Las ventas `Partial` son casas nuevas: su precio no se comporta como el de una casa usada de la misma superficie.
- **Período de crisis.** Las ventas cubren 2006 a 2010, con la crisis hipotecaria de 2008 en medio.

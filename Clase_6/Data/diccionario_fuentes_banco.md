# Diccionario de datos · Caso Banco (Bank Marketing)

**Curso:** Machine Learning · Programa de Especialización Data Scientist · Módulo 2
**Docente:** Josef Renato Rodriguez
**Archivo:** `fuentes_banco.zip` · 5 archivos CSV · separador coma · con encabezado

---

## 1. Qué es

Las llamadas de telemarketing de un banco portugués para vender depósitos a plazo, de **mayo de 2008 a noviembre de 2010** (41 188 llamadas). Para el curso, la tabla original se partió en cinco fuentes, como estarían en un banco, y se pegan con `cliente_id` y `periodo`.

## 2. Fuente

| | |
|---|---|
| Datos originales | Moro, S., Cortez, P. y Rita, P. (2014). A data-driven approach to predict the success of bank telemarketing. *Decision Support Systems*, 62, 22–31. Archivo `bank-additional-full.csv` del UCI Machine Learning Repository. |
| Reconstruido para el curso | `periodo` (a partir del orden cronológico del original), `cliente_id` (el original no tiene identificador) |
| Simulado para el curso | `n_productos_hoy`, `fecha_actualizacion`, las versiones repetidas de algunos clientes en el maestro, los clientes ausentes del maestro y el formato de texto del `cliente_id` en `gestiones` |

## 3. Columnas por fuente

La columna **¿Se conoce?** dice en qué momento está disponible el dato respecto de la llamada.

### `gestiones.csv` · Área de Campañas · una fila por llamada · 41 188 filas

| Columna | Original UCI | Descripción | ¿Se conoce? | Valores | Nulos |
|---|---|---|---|---|---|
| `gestion_id` | — | Identificador de la gestión. | — | — | 0 |
| `cliente_id` | — (creado) | Cliente llamado. **Texto de 8 caracteres con ceros a la izquierda.** | — | — | 0 |
| `periodo` | month (reconstruido) | Mes de la llamada, AAAA-MM. Reconstruido del orden cronológico del archivo original. | antes | 2008-05, 2008-06, 2008-07, 2008-08, 2008-10, 2008-11, 2008-12, 2009-03, 2009-04, 2009-05, 2009-06, 2009-07 … | 0 |
| `canal` | contact | Tipo de teléfono: cellular (celular) o telephone (fijo). | antes | cellular, telephone | 0 |
| `dia_semana` | day_of_week | Día de la semana de la llamada (mon a fri). | antes | fri, mon, thu, tue, wed | 0 |
| `n_llamadas` | campaign | Número de intentos a ese cliente en esta campaña, incluida esta llamada. | durante | 1 – 56 | 0 |
| `duracion_seg` | duration | Duración de la llamada, en segundos. | **al colgar** | 0 – 4918 | 0 |

### `historial_campanas.csv` · CRM · campañas anteriores, una fila por gestión · 41 188 filas

| Columna | Original UCI | Descripción | ¿Se conoce? | Valores | Nulos |
|---|---|---|---|---|---|
| `cliente_id` | — (creado) | Cliente (número). | — | — | 0 |
| `periodo` | — | Mes de la gestión. | — | 2008-05, 2008-06, 2008-07, 2008-08, 2008-10, 2008-11, 2008-12, 2009-03, 2009-04, 2009-05, 2009-06, 2009-07 … | 0 |
| `dias_ultimo_contacto` | pdays | Días desde el último contacto en una campaña anterior. **999 = nunca contactado.** | antes | 0 – 999 | 0 |
| `contactos_previos` | previous | Contactos en campañas anteriores. | antes | 0 – 7 | 0 |
| `resultado_previo` | poutcome | Resultado de la campaña anterior: success, failure o nonexistent. | antes | failure, nonexistent, success | 0 |

### `clientes.csv` · Maestro de clientes · foto extraída en diciembre de 2010 · 41 235 filas

| Columna | Original UCI | Descripción | ¿Se conoce? | Valores | Nulos |
|---|---|---|---|---|---|
| `cliente_id` | — (creado) | Cliente (número). | — | — | 0 |
| `edad` | age | Edad en años. | antes | 17 – 98 | 0 |
| `ocupacion` | job | Ocupación (admin., blue-collar, technician, retired, student…; unknown = sin dato). | antes | admin., blue-collar, entrepreneur, housemaid, management, retired, self-employed, services, student, technician, unemployed, unknown | 0 |
| `estado_civil` | marital | married, single, divorced (incluye viudos), unknown. | antes | divorced, married, single, unknown | 0 |
| `educacion` | education | Nivel educativo; unknown = sin dato. | antes | basic.4y, basic.6y, basic.9y, high.school, illiterate, professional.course, university.degree, unknown | 0 |
| `mora_previa` | default | ¿Tiene créditos en mora? no, yes, unknown. | antes | no, unknown, yes | 0 |
| `hipoteca` | housing | ¿Tiene crédito hipotecario? no, yes, unknown. | antes | no, unknown, yes | 0 |
| `prestamo_consumo` | loan | ¿Tiene préstamo personal? no, yes, unknown. | antes | no, unknown, yes | 0 |
| `n_productos_hoy` | simulada | Productos vigentes del cliente **a la fecha de extracción del maestro** (diciembre de 2010). | **diciembre de 2010** | 1 – 9 | 0 |
| `fecha_actualizacion` | simulada | Fecha de la última actualización del registro. Algunos clientes tienen más de una versión. | — | — | 0 |

### `macro_mensual.csv` · Estudios Económicos · un mes por fila · 27 filas

| Columna | Original UCI | Descripción | ¿Se conoce? | Valores | Nulos |
|---|---|---|---|---|---|
| `periodo` | — | Mes al que corresponde el dato. Solo están los meses que tiene la serie del banco. | — | 2008-04, 2008-05, 2008-06, 2008-07, 2008-08, 2008-10, 2008-11, 2008-12, 2009-03, 2009-04, 2009-05, 2009-06 … | 0 |
| `euribor_3m` | euribor3m | Tasa euribor a 3 meses (%), promedio del mes. | **al cerrar el mes** | 0.6455 – 4.9648 | 0 |
| `var_empleo` | emp.var.rate | Tasa de variación del empleo (trimestral). | al cerrar el mes | -3.4 – 1.4 | 0 |
| `ipc` | cons.price.idx | Índice de precios al consumidor (mensual). | al cerrar el mes | 92.201 – 94.767 | 0 |
| `confianza_consumidor` | cons.conf.idx | Índice de confianza del consumidor (mensual). | al cerrar el mes | -50.8 – -26.9 | 0 |
| `n_empleados` | nr.employed | Número de empleados, en miles (trimestral). | al cerrar el mes | 4963.6 – 5228.1 | 0 |

### `respuestas.csv` · Área de Productos · una fila por gestión · 41 188 filas

| Columna | Original UCI | Descripción | ¿Se conoce? | Valores | Nulos |
|---|---|---|---|---|---|
| `cliente_id` | — (creado) | Cliente (número). | — | — | 0 |
| `periodo` | — | Mes de la gestión. | — | 2008-05, 2008-06, 2008-07, 2008-08, 2008-10, 2008-11, 2008-12, 2009-03, 2009-04, 2009-05, 2009-06, 2009-07 … | 0 |
| `contrato` | y | **Variable objetivo.** 1 si contrató el depósito a plazo, 0 si no. | después de la campaña | 0 – 1 | 0 |

## 4. Advertencias

- El `cliente_id` de `gestiones` es texto; en las demás fuentes es número.
- El maestro tiene clientes repetidos (versiones de distinta fecha) y le faltan algunos clientes que sí aparecen en las gestiones.
- La serie macro no tiene todos los meses: faltan los meses en que el banco no hizo llamadas. `2008-04` se aproximó con el valor de mayo de 2008.
- En `historial_campanas`, 999 en `dias_ultimo_contacto` es un código, no un número de días.
- La tasa de contratación pasa de 5 % en 2008 a 52 % en 2010: el banco cambió a quién llamaba después de la crisis.

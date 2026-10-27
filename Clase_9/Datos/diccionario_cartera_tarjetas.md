# Diccionario de datos · `cartera_tarjetas.csv`

**Curso:** Machine Learning · Programa de Especialización Data Scientist · Clase 9
**Docente:** Josef Renato Rodriguez

Cartera de **tarjetas de crédito** de un banco: una fila por **cliente y mes** (la foto del cliente al cierre del mes).
El objetivo es predecir si el cliente cae en **default en los 3 meses siguientes** a la foto.

> Los datos son **sintéticos**: se generaron con reglas de riesgo realistas para el curso. No corresponden a clientes reales.

## Tamaño y períodos

| | |
|---|---|
| Filas | 54 600 |
| Clientes distintos | 8 986 (cada uno aparece en unos 6 meses) |
| Períodos | 2024-01 a 2026-06 |
| Filas por mes | 1 800 en 2024 y 2025 · 1 900 en 2026 |
| Tasa de default | 6.1 % (2024) · 6.3 % (2025) · 9.7 % (2026-S1) |

**¿Por qué termina en 2026-06?** El target mira 3 meses hacia adelante: la foto de junio necesita julio, agosto y septiembre
para saber si el cliente cayó. Las fotos de julio de 2026 en adelante todavía no tienen el target completo.

## Corte temporal de la Clase 9

| Muestra | Períodos | Uso |
|---|---|---|
| Entrenamiento | 2024-01 a 2024-12 | ajustar los modelos y fijar los cortes de los cinco grupos |
| Test | 2025-01 a 2025-12 | parada temprana y elección de hiperparámetros |
| OOT | 2026-01 a 2026-06 | evaluación final |

## Variables

| # | Variable | Tipo | Descripción | Rango / valores |
|---|---|---|---|---|
| 1 | `id_cliente` | identificador | Código del cliente. **No entra al modelo.** | 100001 a 109000 |
| 2 | `periodo` | fecha (AAAA-MM) | Mes de la foto. **No entra al modelo**; se usa para el corte temporal. | 2024-01 a 2026-06 |
| 3 | `edad` | numérica | Edad del cliente en años, en el mes de la foto. | 21 a 74 |
| 4 | `ingreso_mensual` | numérica | Ingreso mensual declarado, en soles. **Tiene vacíos** (5.2 %), más frecuentes en informales. | S/ 380 a S/ 20 590 |
| 5 | `antiguedad_meses` | numérica | Meses del cliente con el banco. | 0 a 318 |
| 6 | `utilizacion_tc` | numérica | Saldo de la tarjeta / línea de crédito. Puede pasar de 1 si el cliente sobregira. | 0 a 1.15 |
| 7 | `dias_atraso_max_6m` | numérica | Máximo de días de atraso en los últimos 6 meses. 0 = siempre al día. | 0 a 89 |
| 8 | `num_consultas_3m` | numérica (conteo) | Veces que otras entidades consultaron al cliente en la central de riesgos en los últimos 3 meses. | 0 a 9 |
| 9 | `ratio_deuda_ingreso` | numérica | Deuda total en el sistema financiero / ingreso mensual. | 0.02 a 2.93 |
| 10 | `tipo_empleo` | categórica | Situación laboral del cliente. | `dependiente`, `independiente`, `informal` |
| — | **`default_3m`** | **target (0/1)** | **1 si el cliente llega a 90 o más días de atraso en alguno de los 3 meses siguientes a la foto.** | 0 / 1 |

## Notas para el análisis

- **Un mismo cliente aparece en varios meses.** Por eso el corte es por tiempo y no aleatorio, y `id_cliente` nunca es una variable.
- **En 2026 cambia el entorno:** entran más clientes independientes e informales, sube la utilización y la tasa de default
  pasa de ~6 % a ~10 %.
- XGBoost, LightGBM y CatBoost manejan los vacíos de `ingreso_mensual` sin imputar. La regresión logística necesita imputación.

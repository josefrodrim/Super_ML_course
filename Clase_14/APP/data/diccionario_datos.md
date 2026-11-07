# Diccionario de datos — Score de riesgo de tarjetas
Curso Machine Learning · Josef Renato Rodriguez

## riesgo_tarjetas_hist.csv (24,000 filas, 2024-01 a 2025-12, 1,000 clientes por mes)
| Columna | Tipo | Descripción | Rango |
|---|---|---|---|
| id_cliente | texto | Código del cliente | C000001–C059999 |
| periodo | texto AAAAMM | Mes de observación | 202401–202512 |
| edad | entero | Edad en años | 21–75 |
| ingreso_mensual | decimal | Ingreso mensual declarado (S/) | 1,130–30,000 |
| antiguedad_meses | entero | Meses como cliente del banco | 1–240 |
| utilizacion_linea | decimal | % de la línea de crédito usada (puede superar 100) | 0–120 |
| max_dias_atraso_6m | entero | Máximo de días de atraso en los últimos 6 meses | 0–120 |
| consultas_3m | entero | Consultas en centrales de riesgo en los últimos 3 meses | 0–10 |
| default_3m | 0/1 | **Target**: 1 si entra en default en los 3 meses siguientes | 0/1 |

Split: train = 2024 · test = 2025-01 a 2025-06 · OOT = 2025-07 a 2025-12. Tasa de default ≈ 6–7%.

## campana_202611.txt (3,000 filas, separado por `|`)
Clientes de la campaña de noviembre 2026. Mismas columnas sin `default_3m`.
La cartera está más apalancada que en desarrollo (PSI ≈ 0.18): sirve para discutir drift.

Datos sintéticos generados para el curso.

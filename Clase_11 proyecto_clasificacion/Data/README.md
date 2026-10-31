# Proyecto Final — Churn a 3 meses (Banco Andino del Sur)

Curso 7 Machine Learning · P.E. Data Scientist · Docente: Josef Renato Rodriguez

Datos sintéticos de 5,000 clientes observados mes a mes entre 2024-01 y 2026-09.
El enunciado completo, las partes del proyecto y la rúbrica están en el documento del proyecto.

## Archivos (`Data/`)

| Archivo | Grano | Filas |
|---|---|---|
| `clientes.csv` | 1 fila por cliente | 5,000 |
| `productos_mensual.csv` | cliente × mes | 98,819 |
| `transacciones_mensual.csv` | cliente × mes | 99,313 |
| `interacciones_mensual.csv` | cliente × mes (solo meses con interacción) | 31,662 |
| `target_churn.csv` | cliente × mes | 90,571 |

## Ventanas

| Ventana | Periodos | Tasa churn_3m |
|---|---|---|
| Train | 2024-01 a 2024-12 | 5.7% |
| Test | 2025-01 a 2025-12 | 6.9% |
| OOT | 2026-01 a 2026-06 | 8.5% |
| Scoring | 2026-07 a 2026-09 | sin target |

## Diccionario de datos

| Variable | Archivo | Descripción |
|---|---|---|
| id_cliente | todos | Identificador único del cliente |
| periodo | mensuales | Mes de observación (el formato puede variar entre archivos) |
| fecha_alta | clientes | Fecha de inicio de la relación con el banco |
| fecha_nacimiento | clientes | Fecha de nacimiento |
| sexo | clientes | F / M |
| region | clientes | Región de residencia |
| segmento | clientes | Masivo, Preferente o Premium |
| canal_adquisicion | clientes | Canal por el que ingresó el cliente |
| nivel_educativo | clientes | Secundaria, Técnica, Universitaria o Posgrado |
| ingreso_declarado | clientes | Ingreso mensual declarado (S/) |
| fecha_baja | clientes | Fecha en que el cliente cerró su relación con el banco (vacía si sigue activo) |
| motivo_baja | clientes | Motivo registrado al cerrar |
| num_productos | productos | Número de productos activos en el mes |
| tiene_tarjeta_credito | productos | 1 si tiene tarjeta de crédito |
| tiene_prestamo | productos | 1 si tiene un préstamo vigente |
| tiene_cuenta_sueldo | productos | 1 si recibe su sueldo en el banco |
| saldo_pasivo_prom | productos | Saldo promedio del mes en cuentas y depósitos (S/) |
| linea_tc | productos | Línea de la tarjeta de crédito (S/) |
| utilizacion_tc | productos | Deuda de tarjeta / línea, entre 0 y 1 |
| num_trx | transacciones | Número de transacciones del mes |
| monto_trx | transacciones | Monto transado en el mes (S/) |
| pct_trx_digital | transacciones | Proporción de transacciones por app o web |
| logins_app | transacciones | Ingresos a la app en el mes |
| dias_desde_ultima_trx | transacciones | Días desde la última transacción al cierre del mes |
| num_reclamos | interacciones | Reclamos registrados en el mes |
| num_llamadas_callcenter | interacciones | Llamadas al call center en el mes |
| nps_encuesta | interacciones | Nota de 0 a 10 si el cliente fue encuestado ese mes |
| contacto_retencion | interacciones | 1 si el equipo de Retención contactó al cliente en el mes |
| churn_3m | target | 1 si el cliente se da de baja en alguno de los 3 meses siguientes |
| monto_trx_prox_3m | target | Suma de monto_trx de los 3 meses siguientes; vacío si el cliente se fue |

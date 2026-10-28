# Diccionario de datos · `segmentacion_tarjetas.csv`

**Curso:** Machine Learning · Programa de Especialización Data Scientist · Clase 10 (Clustering, partes 1 y 2)
**Docente:** Josef Renato Rodriguez

Comportamiento de uso de la tarjeta de crédito de **los mismos clientes de la cartera de la Clase 9**
(`cartera_tarjetas.csv`): **una fila por cliente**, con sus promedios de **enero a junio de 2026**.
No hay target: la base es para **segmentar** clientes (aprendizaje no supervisado).

> Los datos son **sintéticos**: se generaron con reglas realistas para el curso. No corresponden a clientes reales.

## Tamaño

| | |
|---|---|
| Filas | 6 685 (un cliente por fila) |
| Clientes | los 6 685 de `cartera_tarjetas.csv` con al menos una foto en 2026 |
| Ventana | promedios de 2026-01 a 2026-06 |
| Vacíos | ninguno |

## Variables

| # | Variable | Tipo | Descripción | Rango |
|---|---|---|---|---|
| 1 | `id_cliente` | identificador | Código del cliente, el mismo de `cartera_tarjetas.csv`. **No entra al clustering.** | 100001 a 109000 |
| 2 | `edad` | numérica | Edad en años (de la última foto de 2026). Para **describir** los segmentos. | 23 a 74 |
| 3 | `antiguedad_meses` | numérica | Meses con el banco. Para **describir**. | 24 a 318 |
| 4 | `linea_credito` | numérica | Línea de la tarjeta, en soles. Para **describir**. | S/ 700 a S/ 60 000 |
| 5 | `gasto_mensual_prom` | numérica | Consumo promedio mensual con la tarjeta, en soles. **Muy sesgada.** | S/ 4 a S/ 29 766 |
| 6 | `num_transacciones_mes` | numérica (conteo) | Compras promedio por mes. **Sesgada.** | 1 a 219 |
| 7 | `ticket_promedio` | numérica | Gasto / número de transacciones, en soles. **Sesgada.** | S/ 1.2 a S/ 963 |
| 8 | `pct_supermercado` | proporción | Parte del gasto en supermercados. | 0 a 0.79 |
| 9 | `pct_restaurantes` | proporción | Parte del gasto en restaurantes y delivery. | 0 a 0.61 |
| 10 | `pct_viajes` | proporción | Parte del gasto en aerolíneas, hoteles y agencias. | 0 a 0.64 |
| 11 | `pct_online` | proporción | Parte del gasto en comercio electrónico. | 0 a 0.99 |
| 12 | `utilizacion_prom` | numérica | Saldo / línea, promedio de 2026 (la misma `utilizacion_tc` de la Clase 9, promediada). Puede pasar de 1. | 0 a 1.15 |
| 13 | `pct_pago_saldo` | proporción | Parte del saldo facturado que el cliente paga cada mes. 1 = paga el total («totalero»). | 0 a 1 |
| 14 | `num_avances_6m` | numérica (conteo) | Disposiciones de efectivo con la tarjeta en los 6 meses. **Sesgada.** | 0 a 27 |
| 15 | `pct_operaciones_app` | proporción | Parte de las operaciones del cliente hechas en la app. | 0 a 1 |
| 16 | `meses_sin_uso_6m` | numérica (conteo) | Meses de los 6 sin ninguna compra. | 0 a 6 |

Las cuatro proporciones de rubros no suman 1: el resto del gasto va a otros rubros (tiendas, servicios, salud, etc.).

## Uso en clase

- **Variables para agrupar (12):** de la 5 a la 16. `edad`, `antiguedad_meses` y `linea_credito` se usan solo para **describir**
  los segmentos ya formados.
- **Transformación recomendada:** `np.log1p` a `gasto_mensual_prom`, `num_transacciones_mes`, `ticket_promedio` y
  `num_avances_6m`, y después `StandardScaler` a las 12.
- **Para cruzar con el riesgo:** unir por `id_cliente` con la última foto de 2026 de `cartera_tarjetas.csv` (columna `default_3m`).

## Archivo solo para el docente

`segmentos_reales.csv` tiene el **segmento con el que se generó cada cliente** (6 segmentos más un grupo pequeño de
clientes atípicos). En la realidad esa columna no existe; aquí sirve para medir, en la parte 2, qué algoritmo recupera mejor
los segmentos (índice de Rand ajustado, ARI). **No subirlo al repositorio de los alumnos hasta la parte 2.**

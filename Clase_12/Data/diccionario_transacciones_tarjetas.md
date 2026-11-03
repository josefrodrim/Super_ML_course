# Diccionario de datos · `transacciones_tarjetas.csv.gz` y `comercios.csv`

**Curso:** Machine Learning · Programa de Especialización Data Scientist · Clase 12 (Segmentación RFM)
**Docente:** Josef Renato Rodriguez

Compras con tarjeta de crédito de **los mismos clientes de las Clases 9 y 10** (`cartera_tarjetas.csv` y
`segmentacion_tarjetas.csv`): **una fila por compra**, de **julio de 2025 a septiembre de 2026**.
La misma base se usa después en las clases de **fraude** y **grafos**.

> Los datos son **sintéticos**: se generaron con reglas realistas para el curso. No corresponden a clientes reales.

## Tamaño

| | |
|---|---|
| Filas | 439 025 compras |
| Clientes | 6 685 en la base; 6 365 con al menos una compra hasta el 30/06/2026 |
| Ventana | 2025-07-01 a 2026-09-30 |
| Formato | CSV comprimido con gzip: `pd.read_csv(url, compression="gzip", parse_dates=["fecha_hora"])` |

## `transacciones_tarjetas.csv.gz`

| # | Variable | Tipo | Descripción |
|---|---|---|---|
| 1 | `id_transaccion` | identificador | Código único de la compra, en orden de fecha. |
| 2 | `id_cliente` | identificador | Código del cliente, el mismo de `cartera_tarjetas.csv`. |
| 3 | `fecha_hora` | fecha y hora | Momento de la compra (hora de Lima). |
| 4 | `monto` | numérica | Importe en soles. **Muy sesgada.** |
| 5 | `id_comercio` | identificador | Comercio donde se hizo la compra; se une con `comercios.csv`. |
| 6 | `canal` | categórica | `presencial` (POS) u `online` (web o app). |
| 7 | `id_dispositivo` | identificador | Dispositivo desde el que se hizo la compra online. Vacío en las presenciales. |

## `comercios.csv`

| # | Variable | Tipo | Descripción |
|---|---|---|---|
| 1 | `id_comercio` | identificador | Código del comercio. |
| 2 | `rubro` | categórica | supermercado, restaurantes, tiendas, servicios, salud, combustible, entretenimiento, viajes u online. |
| 3 | `ciudad` | categórica | Ciudad del comercio; `online` para comercios web. |
| 4 | `pais` | categórica | País del comercio. |

## Uso en la Clase 12

- **Fecha de corte:** 30 de junio de 2026. La **historia** (julio 2025 a junio 2026) arma el RFM; julio a septiembre
  de 2026 es el **futuro**, solo para validar.
- **RFM:** `recencia` = días entre la fecha de la última compra y el corte (366 si no compró); `frecuencia` = número de
  compras; `monto` = suma de compras. Partir de la lista de los 6 685 clientes para no perder a los que no compraron.
- **Default:** se une por `id_cliente` con la última foto de 2026 de `cartera_tarjetas.csv` (columna `default_3m`).

## Archivos solo para el docente (carpeta `Solo_docente`)

- `fraude_etiquetas.csv`: las 516 compras fraudulentas que se sembraron en la base, con su patrón (`comercio_comprometido`,
  `tarjeta_clonada`, `prueba_tarjeta`). **No subirlo al repositorio de los alumnos**: es la respuesta de las clases de fraude
  y grafos.
- `generar_transacciones.py`: el script que generó la base (semilla fija).

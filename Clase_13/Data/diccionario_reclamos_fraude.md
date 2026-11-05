# Diccionario de datos · `reclamos_fraude.csv`

**Curso:** Machine Learning · Programa de Especialización Data Scientist · Clase 13 (Fraude: anomalías y grafos)
**Docente:** Josef Renato Rodriguez

Reclamos de clientes por **cargos que no reconocen** en su tarjeta. Una fila por cliente reclamante. Es lo que el banco
**sabe** en cada fecha: un fraude solo se conoce cuando el cliente reclama, días después del cargo.

> Datos **sintéticos**, generados para el curso a partir de los fraudes sembrados en el transaccional de la Clase 12.

## Tamaño

| | |
|---|---|
| Filas | 214 reclamos (uno por cliente) |
| Ventana | reclamos del 12/01/2026 al 30/06/2026 |

## Variables

| # | Variable | Tipo | Descripción |
|---|---|---|---|
| 1 | `id_reclamo` | identificador | Código del reclamo, en orden de fecha. |
| 2 | `id_cliente` | identificador | Cliente que reclama; el mismo de `transacciones_tarjetas.csv.gz`. |
| 3 | `fecha_reclamo` | fecha | Día en que el cliente presentó el reclamo (entre 1 y 15 días después de su último cargo desconocido). |
| 4 | `fecha_primer_cargo` | fecha | Día del primer cargo que el cliente no reconoce. |
| 5 | `n_cargos` | entero | Número de cargos reclamados. |
| 6 | `monto_reclamado` | numérica | Suma de los cargos reclamados, en soles. |

## Archivos que se usan junto con este (carpeta `Clase_12/Data`)

- `transacciones_tarjetas.csv.gz` y `comercios.csv`: el transaccional de la Clase 12 (ver su diccionario).
- `fraude_etiquetas.csv`: las 516 compras confirmadas como fraude, con su patrón (`tarjeta_clonada`,
  `comercio_comprometido`, `prueba_tarjeta`). En la Clase 13 solo se usa para **evaluar** los modelos.

## Uso en la Clase 13

- **Isolation Forest:** se entrena con julio a diciembre de 2025 (sin etiquetas) y se evalúa en enero a septiembre de 2026
  con `fraude_etiquetas.csv`.
- **Punto de compromiso:** con los reclamos recibidos hasta el **20/03/2026**, se buscan los comercios presenciales por
  los que pasaron los reclamantes en los 90 días previos a su `fecha_primer_cargo`.

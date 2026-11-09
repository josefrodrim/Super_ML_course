# score-app — Score de riesgo de tarjetas en producción
Curso Machine Learning · Josef Renato Rodriguez

Modelo de probabilidad de default a 3 meses (6 variables) con bandas Muy alto → Muy bajo,
servido con FastAPI y publicado en Vercel. Incluye scoring de la campaña mensual desde un `.txt`.

## Correr en local
```bash
# Windows
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
# Mac / Linux
python3.12 -m venv .venv
source .venv/bin/activate

pip install -r requirements-dev.txt
python train.py               # genera model/modelo_riesgo.joblib
uvicorn app:app --reload      # http://127.0.0.1:8000  y  /docs
```

## Endpoints
| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/` | Página web |
| GET | `/api/info` | Versión del modelo, cortes y métricas |
| POST | `/api/score` | JSON de un cliente → `prob_default` y `banda` |
| POST | `/api/campana` | Archivo `.txt/.csv` → resumen por banda, PSI y clientes puntuados |

## Publicar en Vercel
Guía completa para alumnos, de inicio a fin: [`../GUIA_PASO_A_PASO.md`](../GUIA_PASO_A_PASO.md).

1. Subir el proyecto a un repo de GitHub (con `model/modelo_riesgo.joblib` incluido).
2. vercel.com → Add New… → Project → importar el repo → Deploy.
3. Cada `git push` a `main` vuelve a desplegar.

## Reglas de oro
- La versión de scikit-learn de `requirements.txt` debe ser la misma con la que entrenaste.
- `requirements.txt` solo lleva lo necesario para servir; lo de desarrollo va en `requirements-dev.txt`.
- Los cortes de las bandas se congelan en desarrollo; no se recalculan por archivo.
- Vercel acepta archivos de hasta ~4.5 MB por petición: suficiente para la campaña de ejemplo.

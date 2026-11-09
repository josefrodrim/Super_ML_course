# Guía paso a paso: del modelo a la web con Vercel

Curso Machine Learning · Josef Renato Rodriguez · Clase 14

Al final de esta guía vas a tener tu propio modelo de riesgo de tarjetas publicado en internet,
con una página web y una API en una dirección como `https://score-tunombre.vercel.app`.

Sigue los pasos **en orden**. Cada paso termina con una verificación: no pases al siguiente
hasta que la tuya salga igual.

---

## Paso 0 · Lo que necesitas instalar (una sola vez)

| Herramienta | Para qué | Cómo comprobar que está |
|---|---|---|
| Python 3.12 | Entrenar el modelo y correr la API | `python --version` (Windows: `py -3.12 --version`) |
| Git | Descargar el proyecto | `git --version` |
| Node.js (versión LTS) | Instalar la herramienta de Vercel | `node --version` |
| Cuenta en [vercel.com](https://vercel.com) | Publicar la app | Entra con tu cuenta de GitHub o tu correo |
| VS Code (recomendado) | Abrir el notebook | — |

---

## Paso 1 · Descargar el proyecto

```bash
git clone https://github.com/josefrodrim/Super_ML_course.git
cd Super_ML_course/Clase_14/APP
```

Si no usas Git: en la página del repositorio, **Code → Download ZIP**, descomprime y abre una terminal
dentro de la carpeta `Clase_14/APP`.

**Verificación:** al listar la carpeta (`ls` en Mac, `dir` en Windows) ves `app.py`, `train.py`,
`requirements.txt`, `data/`, `model/`, `templates/` y `notebooks/`.

> Desde aquí, **todos los comandos se corren dentro de `Clase_14/APP`**.

---

## Paso 2 · Crear el entorno virtual e instalar librerías

**Mac / Linux**
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

**Windows (PowerShell)**
```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
```

Si PowerShell no deja activar el entorno, corre una vez
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a intentarlo.

**Verificación:**
```bash
python -c "import sklearn, fastapi; print(sklearn.__version__, fastapi.__version__)"
```
Debe imprimir `1.9.1 0.162.0`. Si sale otra versión de scikit-learn, **detente**: estás usando
otro Python (revisa que el entorno esté activado; el prompt muestra `(.venv)`).

---

## Paso 3 · Entrenar el modelo

Tienes dos caminos. Ambos generan el archivo `model/modelo_riesgo.joblib`, que es lo que la API usa.

### Opción A · Con el notebook (para entender cada paso)

1. Abre `notebooks/Clase_Puesta_en_Produccion.ipynb` en VS Code.
2. Arriba a la derecha, en **Select Kernel**, elige el Python de tu carpeta `.venv`.
   No elijas otro Python aunque aparezca primero.
3. **Run All**.

**Verificación:** la primera celda de código imprime `(24000, 9) | sklearn 1.9.1`.
Si dice otra versión (por ejemplo `1.8.0`), el kernel no es el de tu `.venv`: cámbialo y vuelve a correr todo.
Esto es importante: un modelo guardado con una versión distinta **no carga** en Vercel.

### Opción B · Con el script (más rápido)

```bash
python train.py
```

**Verificación:** imprime AUC, Gini y KS de train, test y oot, y termina con
`Guardado en .../model/modelo_riesgo.joblib (... KB) sklearn 1.9.1`.

Resultados esperados en ambos casos: AUC test ≈ 0.766 y AUC oot ≈ 0.773.

> Cada vez que corres el notebook o `train.py`, el modelo se **reemplaza**. Es lo esperado.

---

## Paso 4 · Probar la API en tu computadora

```bash
uvicorn app:app --reload
```

Deja esa terminal abierta. Debe decir `Uvicorn running on http://127.0.0.1:8000`.

Abre en el navegador:

- http://127.0.0.1:8000 → la página web con el formulario.
- http://127.0.0.1:8000/docs → la documentación interactiva de la API.

**Prueba 1 · Un cliente.** Abre **otra** terminal (con el entorno activado) dentro de `Clase_14/APP`:

Mac / Linux:
```bash
curl -X POST http://127.0.0.1:8000/api/score -H "Content-Type: application/json" \
  -d '{"edad":35,"ingreso_mensual":3500,"antiguedad_meses":24,"utilizacion_linea":40,"max_dias_atraso_6m":0,"consultas_3m":1}'
```
Windows (PowerShell):
```powershell
curl.exe -X POST http://127.0.0.1:8000/api/score -H "Content-Type: application/json" `
  -d '{\"edad\":35,\"ingreso_mensual\":3500,\"antiguedad_meses\":24,\"utilizacion_linea\":40,\"max_dias_atraso_6m\":0,\"consultas_3m\":1}'
```

**Verificación:** responde `{"prob_default":0.0321,"banda":"Medio"}`.

También puedes correr la celda de la API del notebook (sección 7, "Del notebook a producción"): con la API encendida imprime
el mismo resultado en vez de `La API no está corriendo`.

**Prueba 2 · La campaña del mes.**

```bash
curl -F "archivo=@data/campana_202611.txt" http://127.0.0.1:8000/api/campana
```
(En Windows usa `curl.exe`.) O en la página web, sube `data/campana_202611.txt`.

**Verificación:** 3000 filas válidas, 0 rechazadas, PSI ≈ 0.179, y la banda "Muy alto" con unos 1024 clientes.

Para apagar la API: en la terminal donde corre, presiona `Ctrl + C`.

---

## Paso 5 · Instalar la herramienta de Vercel e iniciar sesión (una sola vez)

```bash
npm install -g vercel
vercel login
```

`vercel login` abre el navegador para que confirmes tu cuenta.

**Verificación:** `vercel whoami` imprime tu usuario de Vercel.

---

## Paso 6 · Crear tu proyecto en Vercel

Dentro de `Clase_14/APP`, elige un nombre **único** (por ejemplo `score-` + tu nombre) y corre:

```bash
vercel link --yes --project score-tunombre
```

**Verificación:** imprime `Created ... score-tunombre`. Aparecen la carpeta `.vercel/` y el archivo `.env.local`.

> `.env.local` guarda una clave de tu cuenta de Vercel. **No la compartas ni la subas a GitHub.**
> El `.gitignore` de la carpeta ya la excluye.

Qué se sube a Vercel lo controla el archivo `.vercelignore` (ya viene en el proyecto):
viaja lo que la API necesita (`app.py`, `requirements.txt`, `model/`, `templates/`).
Los notebooks, `train.py`, los datos de entrenamiento y `.env.local` se quedan en tu computadora.

---

## Paso 7 · Publicar

```bash
vercel deploy
```

Tarda 1 o 2 minutos. Al terminar muestra `readyState: READY` y tu dirección pública,
por ejemplo `https://score-tunombre.vercel.app`.

> El **primer** despliegue de un proyecto nuevo sale directo a producción, con la dirección final.

**Verificación:** abre tu dirección en el navegador y repite las pruebas del Paso 4 cambiando
`http://127.0.0.1:8000` por tu dirección de Vercel:

```bash
curl https://score-tunombre.vercel.app/api/info
curl -F "archivo=@data/campana_202611.txt" https://score-tunombre.vercel.app/api/campana
```

`/api/info` debe mostrar `"sklearn":"1.9.1"` y la versión (fecha y hora) del modelo que entrenaste.

---

## Paso 8 · Actualizar la app cuando cambies el modelo

1. Vuelve a entrenar (Paso 3).
2. Pruébalo en local (Paso 4).
3. Publica la nueva versión:
   ```bash
   vercel deploy --prod
   ```
4. Revisa en `/api/info` que la versión del modelo cambió.

---

## Reglas de oro

- La versión de scikit-learn con la que entrenas **debe ser la misma** de `requirements.txt` (1.9.1).
- `requirements.txt` lleva solo lo necesario para servir la API; lo de desarrollo va en `requirements-dev.txt`.
- Los cortes de las bandas se fijan al entrenar. No se recalculan con cada archivo de campaña.
- Vercel acepta archivos de hasta unos 4.5 MB por petición. La campaña de ejemplo pesa 112 KB.

---

## Si algo falla

| Mensaje | Causa | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'fastapi'` | El entorno no está activado o faltó instalar | Activa `.venv` y corre `pip install -r requirements-dev.txt` |
| La primera celda dice `sklearn 1.8.0` (u otra) | El notebook usa otro Python | En **Select Kernel** elige el de `.venv` y corre todo de nuevo |
| `InconsistentVersionWarning` o `No module named '_loss'` al cargar el modelo | El modelo se entrenó con otra versión de scikit-learn | Vuelve a entrenar con el entorno correcto (Paso 3) |
| `La API no está corriendo: URLError` | `uvicorn` no está encendido | Corre `uvicorn app:app --reload` en otra terminal |
| `address already in use` | Ya hay algo en el puerto 8000 | Cierra la otra API (`Ctrl + C`) o usa `uvicorn app:app --port 8001` |
| `Project name ... already exists` | Alguien ya usa ese nombre | Elige otro nombre en el Paso 6 |
| La página de Vercel da error 500 | Falta el modelo o se subió uno incompatible | Revisa que exista `model/modelo_riesgo.joblib` entrenado con 1.9.1 y vuelve a publicar |
| `413` al subir la campaña | El archivo pasa de ~4.5 MB | Divide el archivo en partes más pequeñas |

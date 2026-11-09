# Super ML Course · Machine Learning Especialización

[![Python](https://img.shields.io/badge/Python-3.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vercel](https://img.shields.io/badge/Vercel-000000?logo=vercel&logoColor=white)](https://vercel.com/)

[🇪🇸 Versión en Español](#-español) | [🇬🇧 English Version](#-english)

---

## 🇪🇸 Español

### 📌 Descripción General
Este repositorio alberga los contenidos, diapositivas, datasets y cuadernos prácticos del **Curso de Machine Learning del Programa de Especialización Data Scientist**, impartido por el docente **Josef Renato Rodriguez**.

El programa combina fundamentos matemáticos e intuitivos con casos de negocio bancarios: tasación inmobiliaria, campañas comerciales, riesgo de crédito, segmentación de clientes, fraude y puesta en producción. Cada sesión trae dos cuadernos Jupyter: una versión de práctica guiada para el estudiante y una versión resuelta (`_SOLUCION.ipynb`).

> Todos los datos bancarios del curso (Clases 6 a 14 y proyecto final) son **sintéticos**: se generaron con reglas realistas y no corresponden a clientes reales.

---

### 🗺️ Estructura del Programa Académico

#### 🔹 Módulo 1: Fundamentos y Modelos de Regresión (Clases 1 a 5)
1. **[Clase 1 · Introducción a Machine Learning](Clase%201/)**
   * **Objetivo:** Diferenciar reglas de negocio programadas a mano frente a reglas aprendidas por modelos.
   * **Contenido:** Árboles de decisión iniciales, métricas básicas de clasificación (accuracy, matriz de confusión).
   * **Datos:** Dataset sintético de 2 000 clientes para predicción de mora bancaria (`ingreso`, `ratio_deuda`, `moroso`).
   * **Archivos:** Presentación y cuadernos (`Clase01_Intro_ML.ipynb` y solución).

2. **[Clase 2 · Regresión Lineal y Métricas](Clase%202/)**
   * **Objetivo:** Predecir variables continuas y cuantificar la magnitud de los errores.
   * **Contenido:** Mínimos Cuadrados Ordinarios (OLS), preprocesamiento (imputación por mediana, One-Hot Encoding), métricas ($MSE$, $RMSE$, $MAE$, $R^2$).
   * **Datos:** `california_housing.csv` con su [diccionario de variables](Clase%202/Datos/diccionario_california_housing.md).
   * **Archivos:** Presentación, datos y cuadernos (`Clase02_Regresion_Lineal.ipynb` y solución).

3. **[Clase 3 · Regularización y Modelos No Lineales](Clase%203/)**
   * **Objetivo:** Evitar sobreajuste y estabilizar coeficientes mediante penalizaciones.
   * **Contenido:** Ridge ($L_2$), Lasso ($L_1$), Support Vector Regressor (SVR), escalado con `StandardScaler`.
   * **Datos:** California Housing.
   * **Archivos:** Presentación y cuadernos (`Clase03_Ridge_Lasso_SVR.ipynb` y solución).

4. **[Clase 4 · Árboles y Ensambles para Regresión](Clase%204/)**
   * **Objetivo:** Modelar relaciones no lineales mediante particiones del espacio de datos.
   * **Contenido:** Árboles de regresión, Random Forest, Gradient Boosting con XGBoost, ajuste de hiperparámetros (`max_depth`, `n_estimators`, `learning_rate`).
   * **Datos:** California Housing.
   * **Archivos:** Presentación y cuadernos (`Clase04_Arboles_RF_XGBoost.ipynb` y solución).

5. **[Clase 5 · Proyecto End-to-End de Regresión](Clase%205%20Proyecto%20Regresion/)**
   * **Objetivo:** Construir un flujo completo desde los datos crudos hasta exportar el modelo.
   * **Contenido:** EDA, ingeniería de variables, selección de modelos, serialización con `joblib` (`modelo_tasacion.joblib`).
   * **Datos:** `ames_housing.csv` (2 930 propiedades en Ames, Iowa) con su [diccionario](Clase%205%20Proyecto%20Regresion/Data/diccionario_ames_housing.md).
   * **Tarea:** Modelo de tasación con `diamonds.csv` ([diccionario](Clase%205%20Proyecto%20Regresion/Tarea/Data/diccionario_diamonds.md)) en [`Tarea_Clase05_EndToEnd.ipynb`](Clase%205%20Proyecto%20Regresion/Tarea/Notebooks/Tarea_Clase05_EndToEnd.ipynb).

---

#### 🔹 Módulo 2: Clasificación y Decisiones de Negocio (Clases 6 a 8)
6. **[Clase 6 · Regresión Logística y Campañas Bancarias](Clase_6/)**
   * **Objetivo:** Priorizar clientes para campañas bajo restricciones de capacidad y desbalance de clases.
   * **Contenido:** Escalera de pegado (unión de varias fuentes), función sigmoide, probabilidades de conversión, métricas en desbalance (Precision, Recall, F1, ROC-AUC).
   * **Datos:** Fuentes relacionales (`clientes.csv`, `gestiones.csv`, `historial_campanas.csv`, `macro_mensual.csv`, `respuestas.csv`, también en `fuentes_banco.zip`) con su [diccionario](Clase_6/Data/diccionario_fuentes_banco.md).
   * **Archivos:** Script `construir_fuentes.py`, gráfico de desbalance, presentación y cuadernos.

7. **[Clase 7 · Árboles, KNN, SVC y Umbral de Decisión](Clase_7/)**
   * **Objetivo:** Elegir clasificador y ajustar el umbral para maximizar la ganancia del negocio.
   * **Contenido:** Árboles de clasificación (Gini vs Entropía), KNN, SVC con kernels, curvas Precision-Recall, umbral óptimo con matriz de costos y beneficios.
   * **Archivos:** Presentación principal, presentación extra sobre modelos locales y fronteras, y cuadernos (`Clase07_Arboles_KNN_SVC_Umbral.ipynb` y solución).

8. **[Clase 8 · Random Forest, XGBoost, LightGBM y CatBoost (Cierre del Módulo 2)](Clase_8/)**
   * **Objetivo:** Comparar ensambles contra los modelos de las clases 6 y 7 sobre la misma campaña y cerrar el módulo.
   * **Contenido:** Random Forest (votación, `min_samples_leaf`, error OOB), importancia por impureza vs por permutación, XGBoost con parada temprana y `scale_pos_weight`, LightGBM (crecimiento por hojas, categorías nativas), CatBoost (categorías sin one-hot), tiempos de entrenamiento, bootstrap de la diferencia de ganancia, preguntas tipo examen.
   * **Datos:** Las fuentes bancarias de la Clase 6 (`Notebooks/fuentes/` y `fuentes_banco.zip`).
   * **Archivos:** Dos versiones de presentación y cuadernos: `Clase08_RandomForest_XGBoost.ipynb` (RF + XGBoost) y `Clase08_RF_XGBoost_LightGBM_CatBoost.ipynb` (versión extendida), cada uno con solución.

---

#### 🔹 Módulo 3: Riesgo de Crédito y Explicabilidad (Clases 9 y 10)
9. **[Clase 9 · Riesgo de Crédito: Boosting y Lift](Clase_9/)**
   * **Objetivo:** Predecir el default a 3 meses de una cartera de tarjetas y ordenar a los clientes por riesgo.
   * **Contenido:** Target a 3 meses, corte temporal (train / test / OOT), XGBoost vs LightGBM vs CatBoost vs logística, tabla de lift en cinco grupos, prueba de monotonía, estabilidad con PSI, probabilidad media vs tasa observada.
   * **Datos:** `cartera_tarjetas.csv` (54 600 filas cliente × mes) con su [diccionario](Clase_9/Datos/diccionario_cartera_tarjetas.md).
   * **Archivos:** Presentación y cuadernos (`Clase09_Riesgo_Boosting_Lift.ipynb` y solución).

10. **[Clase 10 · Explicabilidad e Interpretabilidad](Clase%2010/)** (primera hora)
    * **Objetivo:** Explicar por qué el modelo campeón de la Clase 9 asigna cada riesgo.
    * **Contenido:** *Odds ratios* de la logística, importancia global (XGBoost y permutación), PDP e ICE, valores SHAP (aditividad, *beeswarm*, motivos de un cliente, dependencia, estabilidad por año).
    * **Datos:** `cartera_tarjetas.csv` de la Clase 9.
    * **Archivos:** `PPT/Clase10_Explicabilidad.pptx` y cuadernos (`Clase10_Explicabilidad.ipynb` y solución).

---

#### 🔹 Módulo 4: Aprendizaje No Supervisado y Analítica de Clientes (Clases 10 a 13)
* **[Clase 10 · Clustering, parte 1](Clase%2010/)** (segunda hora)
  * **Objetivo:** Segmentar clientes sin target.
  * **Contenido:** Distancias y escalado, K-Means, inercia y silueta para elegir k, perfilado y nombre de segmentos, cruce con el riesgo, proyección en 2D con PCA.
  * **Datos:** `segmentacion_tarjetas.csv` (los clientes de la Clase 9, una fila por cliente con promedios de enero a junio de 2026) con su [diccionario](Clase%2010/Data/diccionario_segmentacion_tarjetas.md).
  * **Archivos:** `PPT/Clase10_11_Clustering.pptx` y cuadernos (`Clase10_Clustering_Parte1.ipynb` y solución).

* **[Clase 11 · Clustering, parte 2: más allá de K-Means](Clase%2010/)** (en la carpeta `Clase 10/`)
  * **Contenido:** Jerárquico aglomerativo y dendrogramas, DBSCAN y HDBSCAN, mezclas gaussianas (GMM, BIC, pertenencia probabilística), comparación de algoritmos (ARI, NMI, silueta), estabilidad de segmentos, asignación de clientes nuevos, PCA (varianza explicada y cargas).
  * **Datos:** `segmentacion_tarjetas.csv` y `segmentos_reales.csv` (segmentos verdaderos, solo disponibles en clase para validar).
  * **Archivos:** `Clase11_Clustering_Parte2_SOLUCION.ipynb`.

12. **[Clase 12 · Segmentación RFM](Clase_12/)**
    * **Objetivo:** Identificar a los mejores clientes, a los que se van y a los ocasionales a partir de sus compras.
    * **Contenido:** Del transaccional a la tabla RFM, fecha de corte (historia vs futuro), puntajes por quintiles y por cortes de negocio, mapa de segmentos, K-Means sobre RFM, reglas vs clusters, validación con el futuro y acción por segmento.
    * **Datos:** `transacciones_tarjetas.csv.gz` (compras de julio 2025 a septiembre 2026), `comercios.csv` y `fraude_etiquetas.csv`, con su [diccionario](Clase_12/Data/diccionario_transacciones_tarjetas.md).
    * **Archivos:** Presentación y cuadernos (`Clase12_RFM_Segmentacion.ipynb` y solución). Usa Plotly para gráficos interactivos.

13. **[Clase 13 · Fraude: Detección de Anomalías y Grafos](Clase_13/)**
    * **Objetivo:** Detectar fraude con pocas etiquetas y descubrir anillos de fraude.
    * **Contenido:** Tasa de fraude por canal y país, variables relativas al propio cliente y de velocidad, Isolation Forest, precisión@k, comparación con reglas de negocio y LOF, grafo cliente–dispositivo con `networkx`, punto de compromiso, variable de grafo dentro del modelo.
    * **Datos:** `reclamos_fraude.csv` (214 reclamos) con su [diccionario](Clase_13/Data/diccionario_reclamos_fraude.md), más el transaccional de la Clase 12.
    * **Archivos:** Presentación y cuadernos (`Clase13_Fraude_Anomalias_Grafos.ipynb` y solución).

---

#### 🔹 Módulo 5: Puesta en Producción (Clase 14)
14. **[Clase 14 · Del Modelo a la Web con Vercel](Clase_14/)**
    * **Objetivo:** Publicar un score de riesgo de tarjetas como página web y API.
    * **Contenido:** Split temporal, logística vs `HistGradientBoostingClassifier`, bandas de riesgo (Muy alto → Muy bajo) con cortes congelados, serialización con `joblib`, scoring batch de la campaña mensual, PSI, API con FastAPI y despliegue en Vercel, lo que falta para producción real en un banco.
    * **Notebook:** [`Clase_Puesta_en_Produccion.ipynb`](Clase_14/Notebooks/Clase_Puesta_en_Produccion.ipynb).
    * **Guía para alumnos:** [`GUIA_PASO_A_PASO.md`](Clase_14/GUIA_PASO_A_PASO.md), desde la instalación hasta la URL pública.
    * **App (`Clase_14/APP/`):** `train.py` entrena y guarda `model/modelo_riesgo.joblib`; `app.py` sirve la API; `templates/index.html` es la página. Detalle en su [README](Clase_14/APP/README.md).

      | Método | Ruta | Qué hace |
      |---|---|---|
      | GET | `/` | Página web |
      | GET | `/api/info` | Versión del modelo, cortes y métricas |
      | POST | `/api/score` | JSON de un cliente → `prob_default` y `banda` |
      | POST | `/api/campana` | Archivo `.txt/.csv` → resumen por banda, PSI y clientes puntuados |

    * **Datos:** `riesgo_tarjetas_hist.csv` (24 000 filas, 2024-01 a 2025-12), `campana_202611.txt` y su versión puntuada, con su [diccionario](Clase_14/APP/data/diccionario_datos.md).

---

#### 🎓 Proyecto Final · Churn a 3 meses
**[`Clase_11 proyecto_clasificacion/`](Clase_11%20proyecto_clasificacion/)**
* **Caso:** Predecir la fuga de clientes a 3 meses en un banco ficticio (Banco Andino del Sur).
* **Datos:** 5 000 clientes observados mes a mes entre 2024-01 y 2026-09: `clientes.csv`, `productos_mensual.csv`, `transacciones_mensual.csv`, `interacciones_mensual.csv` y `target_churn.csv`. Ventanas, tasas de churn y diccionario en su [README](Clase_11%20proyecto_clasificacion/Data/README.md).
* **Plantilla:** [`Proyecto_Final_Plantilla.ipynb`](Clase_11%20proyecto_clasificacion/Notebooks/Proyecto_Final_Plantilla.ipynb), con partes A a J: integración y limpieza, EDA, ingeniería de variables, fuga de información, esquema de validación, regresión, clasificación, bandas de riesgo y campaña, explicabilidad, drift, clustering, despliegue y recomendación al negocio.

---

### 📂 Estructura de Directorios

```text
Super_ML_course/
├── Clase 1/                          # Intro a ML (Notebook/, PPT/)
├── Clase 2/                          # Regresión lineal (Datos/, Notebooks/, PPT/)
├── Clase 3/                          # Ridge, Lasso, SVR (Notebook/, PPT/)
├── Clase 4/                          # Árboles, RF, XGBoost en regresión (Notebooks/, PPT/)
├── Clase 5 Proyecto Regresion/       # Proyecto end-to-end (Data/, Notebook/, PPT/, Tarea/)
├── Clase_6/                          # Logística y campañas (Data/, Graficos/, Notebooks/, PPT/)
├── Clase_7/                          # Árboles, KNN, SVC, umbral (Notebook/, PPT/)
├── Clase_8/                          # RF, XGBoost, LightGBM, CatBoost (Notebooks/, PPT/)
├── Clase_9/                          # Riesgo de crédito y lift (Datos/, Notebooks/, PPT/)
├── Clase 10/                         # Explicabilidad + Clustering partes 1 y 2 (Data/, Notebook/, PPT/)
├── Clase_11 proyecto_clasificacion/  # Proyecto final de churn (Data/, Notebooks/)
├── Clase_12/                         # Segmentación RFM (Data/, Notebooks/, PPT/)
├── Clase_13/                         # Fraude, anomalías y grafos (Data/, Notebook/, PPT/)
├── Clase_14/                         # Puesta en producción
│   ├── GUIA_PASO_A_PASO.md           # Guía de despliegue para alumnos
│   ├── Notebooks/                    # Notebook de la clase
│   └── APP/                          # App FastAPI lista para Vercel
│       ├── app.py · train.py         # API y entrenamiento
│       ├── data/ · model/            # Datos, diccionario y modelo serializado
│       ├── templates/                # Página web
│       └── requirements*.txt         # Dependencias para servir / desarrollar
├── requirements.txt                  # Dependencias base del curso
└── .gitignore
```

---

### 🚀 Instalación y Uso

#### 1. Clonar el repositorio
```bash
git clone https://github.com/josefrodrim/Super_ML_course.git
cd Super_ML_course
```

#### 2. Crear y activar un entorno virtual
* macOS / Linux:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* Windows:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

#### 3. Instalar librerías
```bash
pip install -r requirements.txt
```
`requirements.txt` trae la base (`numpy`, `pandas`, `matplotlib`, `scikit-learn`, `plotly`, `nbformat`, `ipykernel`) y las librerías de las clases avanzadas. Está probado con Python 3.14. Uso de cada librería adicional:

| Librería | Clases |
|---|---|
| `xgboost` | 4, 5, 8, 9, 10 |
| `lightgbm`, `catboost` | 8, 9 |
| `shap` | 10 |
| `scipy` | 7, 8, 11 |
| `networkx` | 13 |
| `seaborn` | Proyecto final |

#### 4. Lanzar Jupyter
```bash
jupyter lab
# o bien
jupyter notebook
```

#### 5. App de la Clase 14 (entorno propio, Python 3.12)
```bash
cd Clase_14/APP
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python train.py               # genera model/modelo_riesgo.joblib
uvicorn app:app --reload      # http://127.0.0.1:8000 y /docs
```
Para publicar en Vercel, sigue la [guía paso a paso](Clase_14/GUIA_PASO_A_PASO.md).

---
---

## 🇬🇧 English

### 📌 Overview
This repository contains the slides, datasets, and Jupyter notebooks for the **Machine Learning course of the Data Scientist Specialization Program**, taught by instructor **Josef Renato Rodriguez**.

The course pairs mathematical intuition with banking business cases: property appraisal, marketing campaigns, credit risk, customer segmentation, fraud, and model deployment. Every session ships two notebooks: a guided exercise notebook for students and a fully solved one (`_SOLUCION.ipynb`). All course materials are in Spanish.

> All banking data (Classes 6 to 14 and the final project) is **synthetic**: generated with realistic rules, not real customers.

---

### 🗺️ Curriculum

#### 🔹 Module 1: Foundations & Regression (Classes 1–5)
1. **[Class 1 · Introduction to ML](Clase%201/)** — Hand-coded rules vs learned rules, first decision trees, accuracy and confusion matrix. Synthetic loan-default dataset (2,000 customers).
2. **[Class 2 · Linear Regression & Metrics](Clase%202/)** — OLS, median imputation, One-Hot Encoding, $MSE$, $RMSE$, $MAE$, $R^2$. Data: `california_housing.csv` ([dictionary](Clase%202/Datos/diccionario_california_housing.md)).
3. **[Class 3 · Regularization & Non-Linear Regression](Clase%203/)** — Ridge ($L_2$), Lasso ($L_1$), SVR, `StandardScaler`.
4. **[Class 4 · Trees & Ensembles for Regression](Clase%204/)** — Regression trees, Random Forest, XGBoost, hyperparameter tuning.
5. **[Class 5 · End-to-End Regression Project](Clase%205%20Proyecto%20Regresion/)** — EDA, feature engineering, model selection, `joblib` export. Data: `ames_housing.csv` (2,930 homes). Assignment: diamond price model with `diamonds.csv`.

#### 🔹 Module 2: Classification & Business Decisions (Classes 6–8)
6. **[Class 6 · Logistic Regression & Bank Campaigns](Clase_6/)** — Joining relational sources, sigmoid, conversion probabilities, imbalanced metrics (Precision, Recall, F1, ROC-AUC). Includes data builder `construir_fuentes.py`.
7. **[Class 7 · Trees, KNN, SVC & Decision Threshold](Clase_7/)** — Gini vs Entropy, KNN, kernel SVC, Precision-Recall curves, profit-driven threshold tuning.
8. **[Class 8 · Random Forest, XGBoost, LightGBM & CatBoost](Clase_8/)** — RF voting and OOB error, impurity vs permutation importance, XGBoost early stopping and `scale_pos_weight`, LightGBM leaf-wise growth and native categoricals, CatBoost, bootstrap of profit difference, module review. Two notebook versions (RF + XGBoost, and extended with LightGBM/CatBoost).

#### 🔹 Module 3: Credit Risk & Explainability (Classes 9–10)
9. **[Class 9 · Credit Risk: Boosting & Lift](Clase_9/)** — 3-month default target, temporal split (train / test / OOT), XGBoost vs LightGBM vs CatBoost vs logistic, five-group lift table, monotonicity, PSI. Data: `cartera_tarjetas.csv` (54,600 customer-month rows).
10. **[Class 10 · Explainability](Clase%2010/)** — Odds ratios, global importance, PDP and ICE, SHAP (additivity, beeswarm, per-customer reasons, dependence, stability over time).

#### 🔹 Module 4: Unsupervised Learning & Customer Analytics (Classes 10–13)
* **[Class 10 · Clustering, part 1](Clase%2010/)** — Scaling and distances, K-Means, inertia and silhouette, segment profiling, link to risk, PCA view. Data: `segmentacion_tarjetas.csv`.
* **[Class 11 · Clustering, part 2](Clase%2010/)** (stored in `Clase 10/`) — Agglomerative clustering, DBSCAN, HDBSCAN, Gaussian Mixtures (BIC), algorithm comparison (ARI, NMI), segment stability, assigning new customers, PCA loadings.
12. **[Class 12 · RFM Segmentation](Clase_12/)** — From transactions to RFM, cutoff date, quintile and business-rule scores, segment map, K-Means on RFM, validation against future behavior. Data: `transacciones_tarjetas.csv.gz`, `comercios.csv`. Uses Plotly.
13. **[Class 13 · Fraud: Anomaly Detection & Graphs](Clase_13/)** — Customer-relative and velocity features, Isolation Forest, precision@k, LOF and rule baselines, customer–device graph with `networkx`, point of compromise, graph features in the model. Data: `reclamos_fraude.csv` plus Class 12 transactions.

#### 🔹 Module 5: Deployment (Class 14)
14. **[Class 14 · From Model to Web with Vercel](Clase_14/)** — Temporal split, logistic vs `HistGradientBoostingClassifier`, frozen risk bands, `joblib` artifact, monthly batch scoring, PSI, FastAPI app deployed on Vercel. Student guide: [`GUIA_PASO_A_PASO.md`](Clase_14/GUIA_PASO_A_PASO.md). App details: [`APP/README.md`](Clase_14/APP/README.md).

#### 🎓 Final Project · 3-Month Churn
**[`Clase_11 proyecto_clasificacion/`](Clase_11%20proyecto_clasificacion/)** — Predict customer churn for a fictional bank: 5,000 customers tracked monthly from 2024-01 to 2026-09 across five tables. The template notebook covers parts A–J: integration, EDA, feature engineering, leakage, validation design, regression, classification, risk bands, explainability, drift, clustering, deployment, and business recommendation.

---

### 📂 Directory Structure
See the [Spanish section](#-estructura-de-directorios) for the full tree. Each class folder holds `PPT/` (slides), `Notebook(s)/` (student + solution notebooks), and, when needed, `Data/` or `Datos/` with a data dictionary.

---

### 🚀 Getting Started

```bash
git clone https://github.com/josefrodrim/Super_ML_course.git
cd Super_ML_course
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

`requirements.txt` holds the base stack (`numpy`, `pandas`, `matplotlib`, `scikit-learn`, `plotly`, `nbformat`, `ipykernel`) plus the libraries for advanced classes (`xgboost`, `lightgbm`, `catboost`, `shap`, `scipy`, `networkx`, `seaborn`). Tested with Python 3.14.

**Class 14 app** (separate environment, Python 3.12):
```bash
cd Clase_14/APP
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python train.py
uvicorn app:app --reload           # http://127.0.0.1:8000 and /docs
```

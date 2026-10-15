# Super ML Course · Machine Learning Especialización

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

[🇪🇸 Versión en Español](#-español) | [🇬🇧 English Version](#-english)

---

## 🇪🇸 Español

### 📌 Descripción General
Este repositorio alberga los contenidos, diapositivas, datasets y cuadernos prácticos del **Programa de Especialización en Machine Learning (Data Scientist)**, impartido por el docente **Josef Renato Rodriguez**.

El programa combina una fundamentación matemática e intuitiva sólida con la resolución de casos de negocio reales (riesgo crediticio, tasación inmobiliaria y campañas bancarias). Cada sesión se apoya en una estructura dual de cuadernos Jupyter: una versión de práctica guiada para el estudiante y una versión completa resuelta (`_SOLUCION.ipynb`).

---

### 🗺️ Estructura del Programa Académico

El curso está organizado en módulos progresivos:

#### 🔹 Módulo 1: Fundamentos y Modelos de Regresión (Sesiones 1 a 5)
1. **[Clase 1 · Introducción a Machine Learning](Clase%201/)**
   * **Objetivo:** Diferenciar reglas de negocio programadas a mano frente a reglas aprendidas por modelos.
   * **Contenido:** Árboles de decisión iniciales, métricas básicas de clasificación (accuracy, matriz de confusión).
   * **Datos:** Dataset sintético de 2 000 clientes para predicción de mora bancaria (`ingreso`, `ratio_deuda`, `moroso`).
   * **Archivos:** Presentación teórica y cuadernos (`Clase01_Intro_ML.ipynb` y solución).

2. **[Clase 2 · Regresión Lineal y Métricas](Clase%202/)**
   * **Objetivo:** Predecir variables cuantitativas continuas y cuantificar la magnitud de los errores.
   * **Contenido:** Regresión por Mínimos Cuadrados Ordinarios (OLS), preprocesamiento (imputación por mediana, One-Hot Encoding), métricas de evaluación ($MSE$, $RMSE$, $MAE$, $R^2$).
   * **Datos:** `california_housing.csv` con su respectivo [diccionario de variables](Clase%202/Datos/diccionario_california_housing.md).
   * **Archivos:** Presentación, datos y cuadernos (`Clase02_Regresion_Lineal.ipynb` y solución).

3. **[Clase 3 · Regularización y Modelos No Lineales](Clase%203/)**
   * **Objetivo:** Evitar sobreajuste y estabilizar coeficientes mediante penalizaciones.
   * **Contenido:** Regresión Ridge ($L_2$), Regresión Lasso ($L_1$), Support Vector Regressor (SVR), escalado de atributos con `StandardScaler`.
   * **Datos:** California Housing dataset.
   * **Archivos:** Presentación y cuadernos (`Clase03_Ridge_Lasso_SVR.ipynb` y solución).

4. **[Clase 4 · Modelos Basados en Árboles y Ensambles para Regresión](Clase%204/)**
   * **Objetivo:** Modelar relaciones complejas no lineales mediante particiones del espacio de datos.
   * **Contenido:** Árboles de decisión de regresión, Random Forest Regressor, Gradient Boosting con XGBoost, sintonización de hiperparámetros (`max_depth`, `n_estimators`, `learning_rate`).
   * **Datos:** California Housing dataset.
   * **Archivos:** Presentación y cuadernos (`Clase04_Arboles_RF_XGBoost.ipynb` y solución).

5. **[Clase 5 · Proyecto End-to-End de Regresión (Cierre de Módulo)](Clase%205%20Proyecto%20Regresion/)**
   * **Objetivo:** Construir un flujo de Machine Learning completo desde los datos crudos hasta la exportación del artefacto.
   * **Contenido:** Análisis Exploratorio de Datos (EDA), ingeniería de variables, selección de modelos, exportación del modelo final en formato binario con `joblib` (`modelo_tasacion.joblib`).
   * **Datos del Proyecto:** `ames_housing.csv` (2 930 propiedades en Ames, Iowa) con su [diccionario de variables](Clase%205%20Proyecto%20Regresion/Data/diccionario_ames_housing.md).
   * **Tarea Práctica:** Desarrollo autónomo de un modelo de tasación con `diamonds.csv` ([diccionario](Clase%205%20Proyecto%20Regresion/Tarea/Data/diccionario_diamonds.md)) y cuaderno [`Tarea_Clase05_EndToEnd.ipynb`](Clase%205%20Proyecto%20Regresion/Tarea/Notebooks/Tarea_Clase05_EndToEnd.ipynb).

---

#### 🔹 Módulo 2: Clasificación y Analítica Aplicada al Negocio (Sesiones 6 y 7)
6. **[Clase 6 · Regresión Logística y Modelado de Campañas Bancarias](Clase_6/)**
   * **Objetivo:** Priorizar clientes para campañas de marketing bajo restricciones de capacidad operativa y desbalanceo de clases.
   * **Contenido:** Escalera de pegado relacional (unión de múltiples fuentes de datos bancarios), función sigmoide, probabilidades de conversión, métricas de clasificación en desbalance (Precision, Recall, F1, ROC-AUC).
   * **Datos:** Conjunto relacional bancario (`clientes.csv`, `gestiones.csv`, `historial_campanas.csv`, `macro_mensual.csv`, `respuestas.csv`, empaquetados también en `fuentes_banco.zip`) y [diccionario de datos](Clase_6/Data/diccionario_fuentes_banco.md).
   * **Archivos:** Script constructor `construir_fuentes.py`, gráficos de desbalanceo, presentación y cuadernos.

7. **[Clase 7 · Clasificación Avanzada y Optimización del Umbral de Decisión](Clase_7/)**
   * **Objetivo:** Seleccionar el mejor clasificador y ajustar el umbral de decisión para maximizar el retorno económico del negocio.
   * **Contenido:** Árboles de clasificación (criterios Gini vs Entropía), K-Nearest Neighbors (KNN), Support Vector Classifier (SVC con kernels), curvas Precision-Recall, calibración y optimización de umbrales bajo matriz de costos y beneficios.
   * **Archivos:** Presentación regular, presentación complementaria sobre modelos locales/fronteras, y cuadernos (`Clase07_Arboles_KNN_SVC_Umbral.ipynb` y solución).

---

### 📂 Estructura de Directorios

```text
Super_ML_course/
├── Clase 1/                               # Intro a ML y reglas aprendidas
│   ├── Notebook/                          # Cuaderno de estudiante y solución
│   └── PPT/                               # Presentación teórica
├── Clase 2/                               # Regresión Lineal
│   ├── Datos/                             # california_housing.csv y diccionario
│   ├── Notebooks/                         # Cuaderno de estudiante y solución
│   └── PPT/                               # Presentación teórica
├── Clase 3/                               # Ridge, Lasso, SVR
│   ├── Notebook/                          # Cuaderno de estudiante y solución
│   └── PPT/                               # Presentación teórica
├── Clase 4/                               # Árboles, Random Forest, XGBoost
│   ├── Notebooks/                         # Cuaderno de estudiante y solución
│   └── PPT/                               # Presentación teórica
├── Clase 5 Proyecto Regresion/            # Proyecto End-to-End
│   ├── Data/                              # ames_housing.csv y diccionario
│   ├── Notebook/                          # Cuaderno del proyecto, solución y modelo_tasacion.joblib
│   ├── PPT/                               # Presentación teórica
│   └── Tarea/                             # Tarea práctica con dataset diamonds
├── Clase_6/                               # Clasificación y Regresión Logística
│   ├── Data/                              # Fuentes bancarias relacionales y diccionario
│   ├── Graficos/                          # Gráficos de apoyo visual
│   ├── Notebooks/                         # Cuadernos y script de construcción
│   └── PPT/                               # Presentación teórica
├── Clase_7/                               # Árboles, KNN, SVC y optimización de umbral
│   ├── Notebook/                          # Cuaderno de estudiante y solución
│   └── PPT/                               # Presentación y diapositivas extra
├── requirements.txt                       # Lista de dependencias del entorno
└── .gitignore                             # Filtros para Git
```

---

### 🚀 Instalación y Uso

#### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd Super_ML_course
```

#### 2. Crear y activar un entorno virtual
* En macOS / Linux:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* En Windows:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

#### 3. Instalar librerías
```bash
pip install -r requirements.txt
```
*(Nota: Para entornos con Python 3.10 a 3.12, asegúrate de tener instaladas versiones compatibles de `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `xgboost` y `ipykernel`).*

#### 4. Lanzar Jupyter Lab / Notebook
```bash
jupyter lab
# o bien
jupyter notebook
```

---
---

## 🇬🇧 English

### 📌 Overview
This repository contains the learning materials, presentations, datasets, and practical Jupyter notebooks for the **Machine Learning Specialization Program (Data Scientist track)**, taught by instructor **Josef Renato Rodriguez**.

The syllabus bridges solid mathematical intuition with real-world business problem solving (credit risk, property appraisal, and bank marketing campaigns). Every session provides a dual-notebook structure: a guided exercise notebook for the student and a fully solved reference notebook (`_SOLUCION.ipynb`).

---

### 🗺️ Curriculum Breakdown

#### 🔹 Module 1: Foundations & Regression Models (Sessions 1 to 5)
1. **[Class 1 · Introduction to Machine Learning](Clase%201/)**
   * **Goal:** Distinguish between rule-based hardcoded logic and machine-learned decision rules.
   * **Topics:** First decision trees, foundational classification metrics (accuracy, confusion matrix).
   * **Data:** Synthetic dataset of 2,000 retail banking customers for loan default prediction (`ingreso`, `ratio_deuda`, `moroso`).
   * **Files:** Slide deck and notebooks (`Clase01_Intro_ML.ipynb` & solution).

2. **[Class 2 · Linear Regression & Evaluation Metrics](Clase%202/)**
   * **Goal:** Predict continuous target variables and assess error magnitudes.
   * **Topics:** Ordinary Least Squares (OLS), data preprocessing (median imputation, One-Hot Encoding), regression metrics ($MSE$, $RMSE$, $MAE$, $R^2$).
   * **Data:** `california_housing.csv` along with its [feature dictionary](Clase%202/Datos/diccionario_california_housing.md).
   * **Files:** Slide deck, data, and notebooks (`Clase02_Regresion_Lineal.ipynb` & solution).

3. **[Class 3 · Regularization & Non-Linear Regression](Clase%203/)**
   * **Goal:** Mitigate overfitting and stabilize model coefficients using shrinkage penalties.
   * **Topics:** Ridge Regression ($L_2$), Lasso Regression ($L_1$), Support Vector Regressor (SVR), feature standardization via `StandardScaler`.
   * **Data:** California Housing dataset.
   * **Files:** Slide deck and notebooks (`Clase03_Ridge_Lasso_SVR.ipynb` & solution).

4. **[Class 4 · Tree-Based Models & Regression Ensembles](Clase%204/)**
   * **Goal:** Model complex non-linear patterns through hierarchical partitions of feature space.
   * **Topics:** Regression Trees, Random Forest Regressor, Gradient Boosting with XGBoost, hyperparameter tuning (`max_depth`, `n_estimators`, `learning_rate`).
   * **Data:** California Housing dataset.
   * **Files:** Slide deck and notebooks (`Clase04_Arboles_RF_XGBoost.ipynb` & solution).

5. **[Class 5 · End-to-End Regression Project (Module Wrap-up)](Clase%205%20Proyecto%20Regresion/)**
   * **Goal:** Execute a comprehensive ML workflow from raw data ingestion to production-ready artifact export.
   * **Topics:** Exploratory Data Analysis (EDA), feature engineering, model selection, model serialization with `joblib` (`modelo_tasacion.joblib`).
   * **Project Data:** `ames_housing.csv` (2,930 home sales in Ames, Iowa) and its [data dictionary](Clase%205%20Proyecto%20Regresion/Data/diccionario_ames_housing.md).
   * **Hands-on Assignment:** Independent diamond price appraisal model using `diamonds.csv` ([dictionary](Clase%205%20Proyecto%20Regresion/Tarea/Data/diccionario_diamonds.md)) and [`Tarea_Clase05_EndToEnd.ipynb`](Clase%205%20Proyecto%20Regresion/Tarea/Notebooks/Tarea_Clase05_EndToEnd.ipynb).

---

#### 🔹 Module 2: Classification & Business Decision Modeling (Sessions 6 & 7)
6. **[Class 6 · Logistic Regression & Bank Campaign Targeting](Clase_6/)**
   * **Goal:** Prioritize lead contact lists under operational capacity constraints and class imbalance.
   * **Topics:** Relational merging pipeline ("escalera de pegado"), sigmoid link function, conversion probabilities, imbalanced classification metrics (Precision, Recall, F1, ROC-AUC).
   * **Data:** Relational banking tables (`clientes.csv`, `gestiones.csv`, `historial_campanas.csv`, `macro_mensual.csv`, `respuestas.csv`, also bundled in `fuentes_banco.zip`) with [documentation](Clase_6/Data/diccionario_fuentes_banco.md).
   * **Files:** Data synthesis script `construir_fuentes.py`, charts, slide deck, and notebooks.

7. **[Class 7 · Advanced Classification & Decision Threshold Optimization](Clase_7/)**
   * **Goal:** Select optimal classifiers and tune probability thresholds to maximize commercial profitability.
   * **Topics:** Classification Trees (Gini vs Entropy impurity), K-Nearest Neighbors (KNN), Support Vector Classifier (SVC with kernel methods), Precision-Recall trade-off, cost/benefit matrix threshold tuning.
   * **Files:** Main presentation, supplementary presentation on local models & decision boundaries, and notebooks (`Clase07_Arboles_KNN_SVC_Umbral.ipynb` & solution).

---

### 📂 Directory Structure

```text
Super_ML_course/
├── Clase 1/                               # Intro to ML & learned rules
│   ├── Notebook/                          # Student & solution notebooks
│   └── PPT/                               # Lecture slides
├── Clase 2/                               # Linear Regression
│   ├── Datos/                             # california_housing.csv & dictionary
│   ├── Notebooks/                         # Student & solution notebooks
│   └── PPT/                               # Lecture slides
├── Clase 3/                               # Ridge, Lasso, SVR
│   ├── Notebook/                          # Student & solution notebooks
│   └── PPT/                               # Lecture slides
├── Clase 4/                               # Trees, Random Forest, XGBoost
│   ├── Notebooks/                         # Student & solution notebooks
│   └── PPT/                               # Lecture slides
├── Clase 5 Proyecto Regresion/            # End-to-End Project
│   ├── Data/                              # ames_housing.csv & dictionary
│   ├── Notebook/                          # Project notebook, solution & modelo_tasacion.joblib
│   ├── PPT/                               # Lecture slides
│   └── Tarea/                             # Assignment with diamonds dataset
├── Clase_6/                               # Classification & Logistic Regression
│   ├── Data/                              # Relational banking sources & dictionary
│   ├── Graficos/                          # Visual aids & balance charts
│   ├── Notebooks/                         # Notebooks & data builder script
│   └── PPT/                               # Lecture slides
├── Clase_7/                               # Trees, KNN, SVC & Threshold tuning
│   ├── Notebook/                          # Student & solution notebooks
│   └── PPT/                               # Lecture and extra boundary slides
├── requirements.txt                       # Python dependencies
└── .gitignore                             # Git ignore rules
```

---

### 🚀 Getting Started

#### 1. Clone the repository
```bash
git clone <REPOSITORY_URL>
cd Super_ML_course
```

#### 2. Set up a virtual environment
* On macOS / Linux:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* On Windows:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```
*(Tip: For Python 3.10–3.12 environments, make sure to install compatible versions of `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `xgboost`, and `ipykernel`).*

#### 4. Launch Jupyter Lab / Notebook
```bash
jupyter lab
# or
jupyter notebook
```

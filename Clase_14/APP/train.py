"""
train.py — Entrena el modelo de riesgo y guarda el artefacto para producción.
Curso Machine Learning · Josef Renato Rodriguez

Uso:  python train.py
Genera: model/modelo_riesgo.joblib
"""
from datetime import datetime
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score

BASE = Path(__file__).parent
DATA = BASE / "data" / "riesgo_tarjetas_hist.csv"
SALIDA = BASE / "model" / "modelo_riesgo.joblib"

FEATURES = ["edad", "ingreso_mensual", "antiguedad_meses",
            "utilizacion_linea", "max_dias_atraso_6m", "consultas_3m"]
TARGET = "default_3m"
# Restricciones monótonas: +1 = a mayor valor, mayor riesgo; -1 = menor riesgo
MONOTONIA = [-1, -1, -1, +1, +1, +1]
BANDAS = ["Muy bajo", "Bajo", "Medio", "Alto", "Muy alto"]


def ks(y, p):
    df = pd.DataFrame({"y": y, "p": p}).sort_values("p")
    cum_bad = (df.y == 1).cumsum() / (df.y == 1).sum()
    cum_good = (df.y == 0).cumsum() / (df.y == 0).sum()
    return float((cum_bad - cum_good).abs().max())


def main():
    df = pd.read_csv(DATA, dtype={"periodo": str})
    train = df[df.periodo < "202501"]
    test = df[(df.periodo >= "202501") & (df.periodo < "202507")]
    oot = df[df.periodo >= "202507"]

    modelo = HistGradientBoostingClassifier(
        max_iter=300, learning_rate=0.05, max_leaf_nodes=15,
        min_samples_leaf=80, l2_regularization=1.0,
        monotonic_cst=MONOTONIA, random_state=42)
    modelo.fit(train[FEATURES], train[TARGET])

    # Cortes de bandas: quintiles del score en TRAIN (se congelan)
    p_train = modelo.predict_proba(train[FEATURES])[:, 1]
    cortes = np.quantile(p_train, [0.2, 0.4, 0.6, 0.8]).tolist()

    metricas = {}
    for nombre, d in [("train", train), ("test", test), ("oot", oot)]:
        p = modelo.predict_proba(d[FEATURES])[:, 1]
        auc = roc_auc_score(d[TARGET], p)
        metricas[nombre] = {"auc": round(auc, 4), "gini": round(2 * auc - 1, 4),
                            "ks": round(ks(d[TARGET].values, p), 4), "n": len(d)}
        print(f"{nombre:>5}  AUC={auc:.3f}  Gini={2*auc-1:.3f}  KS={metricas[nombre]['ks']:.3f}")

    artefacto = {
        "modelo": modelo,
        "features": FEATURES,
        "cortes": cortes,
        "bandas": BANDAS,
        "metricas": metricas,
        "version": datetime.now().strftime("%Y%m%d-%H%M"),
        "sklearn_version": sklearn.__version__,
    }
    SALIDA.parent.mkdir(exist_ok=True)
    joblib.dump(artefacto, SALIDA, compress=3)
    print(f"\nCortes (quintiles train): {[round(c, 4) for c in cortes]}")
    print(f"Guardado en {SALIDA}  ({SALIDA.stat().st_size/1024:.0f} KB)  sklearn {sklearn.__version__}")


if __name__ == "__main__":
    main()

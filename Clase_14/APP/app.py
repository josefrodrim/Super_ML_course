"""
app.py — API de scoring de riesgo (FastAPI) lista para Vercel.
Curso Machine Learning · Josef Renato Rodriguez

Local:   uvicorn app:app --reload   →  http://127.0.0.1:8000
Docs:    http://127.0.0.1:8000/docs
"""
import io
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

BASE = Path(__file__).parent
ART = joblib.load(BASE / "model" / "modelo_riesgo.joblib")  # se carga UNA vez al iniciar
MODELO, FEATURES, CORTES, BANDAS = ART["modelo"], ART["features"], ART["cortes"], ART["bandas"]

RANGOS = {  # validación de entrada: (mínimo, máximo)
    "edad": (18, 100), "ingreso_mensual": (0, 500000), "antiguedad_meses": (0, 600),
    "utilizacion_linea": (0, 150), "max_dias_atraso_6m": (0, 360), "consultas_3m": (0, 50),
}

app = FastAPI(title="Score de riesgo · Tarjetas", version=ART["version"])


class Cliente(BaseModel):
    edad: int = Field(..., ge=18, le=100, examples=[35])
    ingreso_mensual: float = Field(..., ge=0, le=500000, examples=[3500])
    antiguedad_meses: int = Field(..., ge=0, le=600, examples=[24])
    utilizacion_linea: float = Field(..., ge=0, le=150, examples=[65])
    max_dias_atraso_6m: int = Field(..., ge=0, le=360, examples=[0])
    consultas_3m: int = Field(..., ge=0, le=50, examples=[2])


def asignar_banda(prob):
    """Cortes congelados en desarrollo: no se recalculan con cada archivo."""
    idx = np.searchsorted(CORTES, prob, side="right")
    return [BANDAS[i] for i in np.atleast_1d(idx)]


@app.get("/", response_class=HTMLResponse)
def inicio():
    return (BASE / "templates" / "index.html").read_text(encoding="utf-8")


@app.get("/api/info")
def info():
    return {"version": ART["version"], "sklearn": ART["sklearn_version"],
            "features": FEATURES, "cortes": CORTES, "metricas": ART["metricas"]}


@app.post("/api/score")
def score(cliente: Cliente):
    X = pd.DataFrame([cliente.model_dump()])[FEATURES]
    prob = float(MODELO.predict_proba(X)[0, 1])
    return {"prob_default": round(prob, 4), "banda": asignar_banda(prob)[0]}


@app.post("/api/campana")
async def campana(archivo: UploadFile = File(...)):
    contenido = await archivo.read()
    try:
        texto = contenido.decode("utf-8-sig", errors="replace")
        cabecera = texto.splitlines()[0]
        sep = max(["|", ",", ";", "\t"], key=cabecera.count)  # separador más frecuente en la cabecera
        df = pd.read_csv(io.StringIO(texto), sep=sep, dtype={"periodo": str, "id_cliente": str})
    except Exception as e:
        raise HTTPException(400, f"No se pudo leer el archivo: {e}")

    df.columns = [c.strip().lower() for c in df.columns]
    faltan = [c for c in ["id_cliente"] + FEATURES if c not in df.columns]
    if faltan:
        raise HTTPException(400, f"Faltan columnas: {', '.join(faltan)}")

    X = df[FEATURES].apply(pd.to_numeric, errors="coerce")
    invalido = X.isna().any(axis=1)
    for col, (lo, hi) in RANGOS.items():
        invalido |= ~X[col].between(lo, hi)

    ok = df[~invalido].copy()
    ok["prob_default"] = MODELO.predict_proba(X[~invalido])[:, 1].round(4)
    ok["banda"] = asignar_banda(ok["prob_default"].values)

    orden = BANDAS[::-1]  # Muy alto primero
    resumen = (ok.groupby("banda").agg(clientes=("id_cliente", "size"),
                                       prob_media=("prob_default", "mean"))
                 .reindex(orden).fillna(0).reset_index())
    resumen["pct"] = (resumen.clientes / max(len(ok), 1) * 100).round(1)
    resumen["prob_media"] = resumen.prob_media.round(4)
    resumen["clientes"] = resumen.clientes.astype(int)

    # PSI contra el desarrollo: en train cada banda tiene 20% por construcción
    a = np.clip(resumen.pct.values / 100, 1e-4, None)
    psi = float(np.sum((a - 0.2) * np.log(a / 0.2)))

    ok["_o"] = ok.banda.map({b: i for i, b in enumerate(orden)})
    ok = ok.sort_values(["_o", "prob_default"], ascending=[True, False]).drop(columns="_o")
    return {
        "archivo": archivo.filename,
        "filas_leidas": int(len(df)),
        "filas_validas": int(len(ok)),
        "filas_rechazadas": int(invalido.sum()),
        "ids_rechazados": df.loc[invalido, "id_cliente"].astype(str).head(50).tolist(),
        "resumen": resumen.to_dict(orient="records"),
        "psi": round(psi, 4),
        "clientes": ok[["id_cliente"] + FEATURES + ["prob_default", "banda"]].to_dict(orient="records"),
    }

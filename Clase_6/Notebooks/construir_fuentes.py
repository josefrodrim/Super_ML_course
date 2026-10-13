"""Construye las 5 fuentes del caso Banco (mayo 2008 - noviembre 2010) a partir de UCI Bank Marketing.
Es determinista (semilla 42): vuelve a generar exactamente los mismos IDs de cliente, que reutilizaremos para los meses de 2011."""
import numpy as np, pandas as pd, os
SEED = 42; rng = np.random.default_rng(SEED)
URL = "https://raw.githubusercontent.com/selva86/datasets/master/bank-additional-full.csv"   # copia de UCI bank-additional-full
d = pd.read_csv("bank.csv" if os.path.exists("bank.csv") else URL, sep=";")
MES = {'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
mm = d.month.map(MES).values; yr = 2008; ys = []; prev = mm[0]
for v in mm:
    if v < prev: yr += 1
    ys.append(yr); prev = v
d["periodo"] = [f"{y}-{v:02d}" for y, v in zip(ys, mm)]
d["y"] = (d.y == "yes").astype(int)
# IDs de cliente aleatorios (una fila = un cliente en el histórico)
ids = rng.choice(np.arange(100000, 999999), len(d), replace=False); d["cliente_id"] = ids
d["gestion_id"] = np.arange(1, len(d) + 1)
os.makedirs("fuentes", exist_ok=True)
# 1. gestiones (id como texto con ceros a la izquierda)
g = pd.DataFrame({"gestion_id": d.gestion_id, "cliente_id": d.cliente_id.map(lambda x: f"{x:08d}"), "periodo": d.periodo,
                  "canal": d.contact, "dia_semana": d.day_of_week, "n_llamadas": d.campaign, "duracion_seg": d.duration})
g.to_csv("fuentes/gestiones.csv", index=False)
# 2. historial de campañas anteriores (CRM)
h = pd.DataFrame({"cliente_id": d.cliente_id, "periodo": d.periodo, "dias_ultimo_contacto": d.pdays,
                  "contactos_previos": d.previous, "resultado_previo": d.poutcome})
h.sample(frac=1, random_state=SEED).to_csv("fuentes/historial_campanas.csv", index=False)
# 3. maestro de clientes: foto extraída en diciembre 2010
base_prod = rng.poisson(1.0, len(d)) + 1
c = pd.DataFrame({"cliente_id": d.cliente_id, "edad": d.age, "ocupacion": d.job, "estado_civil": d.marital, "educacion": d.education,
                  "mora_previa": d["default"], "hipoteca": d.housing, "prestamo_consumo": d.loan,
                  "n_productos_hoy": base_prod + d.y.values})
dias = rng.integers(0, (pd.Timestamp("2010-12-15") - pd.Timestamp("2009-01-01")).days, len(c))
c["fecha_actualizacion"] = (pd.Timestamp("2009-01-01") + pd.to_timedelta(dias, unit="D")).strftime("%Y-%m-%d")
# versiones viejas duplicadas (350 clientes): educación aún sin registrar, fecha anterior
dup = c.sample(350, random_state=SEED).copy()
dup["educacion"] = "unknown"; dup["fecha_actualizacion"] = "2008-03-31"
# clientes huérfanos: 300 que no están en el maestro
huerf = c.sample(300, random_state=SEED + 1).cliente_id
c = pd.concat([c[~c.cliente_id.isin(huerf)], dup[~dup.cliente_id.isin(huerf)]]).sample(frac=1, random_state=SEED)
c.to_csv("fuentes/clientes.csv", index=False)
# 4. macro mensual: promedio del mes, solo meses publicados en la serie que tiene el banco
mac = d.groupby("periodo")[["euribor3m", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "nr.employed"]].mean().reset_index()
mac.columns = ["periodo", "euribor_3m", "var_empleo", "ipc", "confianza_consumidor", "n_empleados"]
abr = mac.iloc[[0]].copy(); abr["periodo"] = "2008-04"   # el mes anterior al inicio: se aproxima con mayo
mac = pd.concat([abr, mac]).round(4)
mac.to_csv("fuentes/macro_mensual.csv", index=False)
# 5. respuestas
r = pd.DataFrame({"cliente_id": d.cliente_id, "periodo": d.periodo, "contrato": d.y}).sample(frac=1, random_state=SEED + 2)
r.to_csv("fuentes/respuestas.csv", index=False)
d[["cliente_id", "gestion_id", "periodo", "y"]].to_csv("llaves_internas.csv", index=False)   # para el generador 2011
for f in sorted(os.listdir("fuentes")): print(f, pd.read_csv("fuentes/" + f).shape)
print("huérfanos", len(huerf), "duplicados", 350 - dup.cliente_id.isin(huerf).sum())
print(mac.to_string())

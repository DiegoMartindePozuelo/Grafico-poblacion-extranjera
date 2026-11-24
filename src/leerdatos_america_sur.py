
from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


raiz = Path(__file__).parent.parent
archivo_excel = raiz / "datos" / "población_extranjera_españa.xlsx"

df = pd.read_excel(archivo_excel, header=None)

matriz = np.array([
    df.iloc[7, 1:26],
    df.iloc[2096, 1:26]
], dtype=int)

anios = matriz[0][::-1]
poblacion = matriz[1][::-1]

df_exportar = pd.DataFrame({
    "Años": anios,
    "Poblacion": poblacion
})

archivo_csv = raiz / "datos" / "Poblacion_AmSur_clm.csv"
archivo_db = raiz / "datos" / "Poblacion_AmSur_clm.db"

df_exportar.to_csv(archivo_csv, index=False)

conexion = sqlite3.connect(archivo_db)
df_exportar.to_sql(
    "evolucion_poblacion_america_sur_clm",
    conexion,
    if_exists="replace",
    index=False
)
conexion.close()

print(matriz)
print("\nDimensiones:", matriz.shape)
print("\nDatos exportados:")
print(df_exportar)

plt.figure(figsize=(9, 5))
plt.plot(anios, poblacion, marker="o", linestyle="-")
plt.title("Población de América del Sur en Castilla-La Mancha")
plt.xlabel("Año")
plt.ylabel("Número de personas")
plt.xticks(anios, rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(raiz / "Grafico_poblacion_america_sur_clm.png")
plt.show()


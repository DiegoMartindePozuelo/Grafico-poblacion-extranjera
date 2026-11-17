from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raiz = Path(__file__).parent.parent

archivo = raiz / "datos" / "población_extranjera_españa.xlsx"

# adgsajdgasjd
df = pd.read_excel(archivo, header=None)

matriz = np.array([
    df.iloc[7, 1:26],
    df.iloc[9, 1:26]
], dtype=int)

print(matriz)

print("\nDimensiones:", matriz.shape)


anios = matriz[0][::-1]
poblacion = matriz[1][::-1]

print("\n========== GRAFICO DE LINEAS ==========")

plt.figure(figsize=(9, 5))
plt.plot(anios, poblacion, marker="o", linestyle="-")
plt.title("Evolución de la población extranjera en España")
plt.xlabel("Año")
plt.ylabel("Número de personas")
plt.xticks(anios, rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

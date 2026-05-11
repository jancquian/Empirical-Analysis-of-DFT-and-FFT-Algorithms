import time
import random
import matplotlib.pyplot as plt
import math

import FFT_C as fft_c
import FFT_NUMPY as fft_n
import DFT as dft
import DFT_REC as dft_r
import DFT_MAT as dft_m


# =========================
# tamaños
# =========================
# CON 2^11 se muere la versión recursiva
sizes = [2**i for i in range(0, 15)]  # ajusta si quieres más grande

signals = []
for n in sizes:
    signals.append([random.random() for _ in range(n)])


# =========================
# ALGORITMOS A COMPARAR
# =========================
algorithms = {
    "FFT_C": fft_c.FFT_C,
    "FFT_NumPy": fft_n.FFT_NUMPY,
    "DFT": dft.DFT,
    #"DFT_Rec": dft_r.DFT_REC,
    "DFT_Mat": dft_m.DFT_MAT
    # puedes agregar más aquí:
    # "FFT_Otro": otro_fft_class
}


# =========================
# MEDICIÓN
# =========================
results = {name: [] for name in algorithms}

for i, signal in enumerate(signals):

    for name, fft_class in algorithms.items():

        fft_instance = fft_class(signal)

        start = time.time()
        fft_instance.compute()
        end = time.time()

        results[name].append(end - start)

##########################

max_time = max(max(v) for v in results.values())


def normalize(curve):
    return [t / max(curve) * max_time for t in curve]

# O(n)
O_n = normalize(sizes)

# O(n log n)
O_nlogn = normalize([n * math.log2(n) for n in sizes])

# O(n²) -> DFT
O_n2 = normalize([n**2 for n in sizes])

# =========================
# GRAFICAR
# =========================
plt.figure(figsize=(10, 6))

for name, times in results.items():
    plt.plot(sizes, times, marker='o', label=name)

#Descomentar para graficar las curvas teoricas 
#plt.plot(sizes, O_n, '--', label='O(n)')
#plt.plot(sizes, O_nlogn, '--', label='O(n log n)')
#plt.plot(sizes, O_n2, '--', label='O(n²)')

plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de complejidad empírica de FFT")
plt.legend()
plt.grid()
plt.show()
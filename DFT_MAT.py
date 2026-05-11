import numpy as np

class DFT_MAT:
    def __init__(self, signal):
        self.x = np.array(signal, dtype=complex)

    def compute(self):
        N = len(self.x)

        # matriz de índices
        n = np.arange(N)
        k = n.reshape((N, 1))

        # matriz de Fourier
        W = np.exp(-2j * np.pi * k * n / N)

        # producto matriz-vector
        return np.dot(W, self.x)
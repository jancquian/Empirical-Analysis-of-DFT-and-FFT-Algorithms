# DFT “naive” o de fuerza bruta (implementación iterativa clásica) O(n²)
import cmath

class DFT:
    def __init__(self, signal):
        self.signal = signal

    def compute(self):
        N = len(self.signal)
        X = []

        for k in range(N):
            sum_val = 0
            for n in range(N):
                angle = -2j * cmath.pi * k * n / N
                sum_val += self.signal[n] * cmath.exp(angle)

            X.append(sum_val)

        return X
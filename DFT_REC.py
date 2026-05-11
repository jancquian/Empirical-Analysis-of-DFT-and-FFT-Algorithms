import cmath

class DFT_REC:
    def __init__(self, signal):
        self.signal = signal

    def compute(self):
        N = len(self.signal)
        return [self._compute_k(k, 0, N) for k in range(N)]

    def _compute_k(self, k, n, N):
        # caso base: terminamos la suma
        if n == N:
            return 0

        angle = -2j * cmath.pi * k * n / N
        current = self.signal[n] * cmath.exp(angle)

        # llamada recursiva sumando el siguiente término
        return current + self._compute_k(k, n + 1, N)
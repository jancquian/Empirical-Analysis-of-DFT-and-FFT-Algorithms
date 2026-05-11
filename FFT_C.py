# FFT de Cooley–Tukey (recursiva); C de fondo; O(nlog(n))
import cmath

class FFT_C:
    def __init__(self, signal):
        self.signal = signal

    def compute(self):
        return self._fft(self.signal)

    def _fft(self, x):
        n = len(x)

        # Caso base
        if n == 1:
            return x

        # Dividir en pares e impares
        even = self._fft(x[0::2])
        odd = self._fft(x[1::2])

        # Factor complejo
        factor = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]

        # Combinar
        return [even[k] + factor[k] for k in range(n // 2)] + \
               [even[k] - factor[k] for k in range(n // 2)]

'''
# Ejemplo de uso
if __name__ == "__main__":
    signal = [0, 1, 2, 3]
    fft = FFT(signal)
    result = fft.compute()

    print("FFT:", result)
'''
# FFT de Numpy; C + Fortran optimizados. Debajo de O(nlog(n))
import numpy as np

class FFT_NUMPY:
    def __init__(self, signal):
        self.signal = np.array(signal, dtype=complex)

    def compute(self):
        return np.fft.fft(self.signal)
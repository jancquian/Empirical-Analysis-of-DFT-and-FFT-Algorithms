# Empirical-Analysis-of-DFT-and-FFT-Algorithms
This project implements several algorithms for computing the Discrete Fourier Transform (DFT) and the Fast Fourier Transform (FFT) in Python and performs an empirical comparison of their execution time using signals of increasing size. The results illustrate the practical differences between O(n2 ) and O(nlogn) algorithms.

## Overview

This project implements several approaches for computing the **Discrete Fourier Transform (DFT)** and the **Fast Fourier Transform (FFT)** in Python.

The objective is to perform an **empirical analysis of algorithmic complexity** by measuring execution times for signals of increasing size and comparing the observed behavior with the expected theoretical complexity.

The project includes both educational implementations (naive DFT) and optimized algorithms (FFT and NumPy FFT).

---

## Implemented Algorithms

### 1. Naive DFT

File: `DFT.py`

This implementation follows the direct mathematical definition of the Discrete Fourier Transform using nested loops.

Time complexity:

O(n²)

This implementation is mainly intended for educational purposes.

---

### 2. Matrix-based DFT

File: `DFT_MAT.py`

This method constructs the **Fourier matrix** and computes the transform using matrix-vector multiplication with NumPy.

Approximate complexity:

O(n²)

---

### 3. Recursive DFT

File: `DFT_REC.py`

A recursive implementation of the DFT equation.

Time complexity:

O(n²)

Note: This implementation becomes inefficient for large input sizes due to recursion depth and computational cost.

---

### 4. FFT using the Cooley–Tukey Algorithm

File: `FFT_C.py`

This implementation applies the **Cooley–Tukey Fast Fourier Transform algorithm**, which recursively splits the signal into even and odd components.

Time complexity:

O(n log n)

---

### 5. FFT using NumPy

File: `FFT_NUMPY.py`

Uses the optimized NumPy implementation:

`numpy.fft.fft()`

This version is highly optimized and implemented in **C and Fortran**, providing significantly better performance.

---

## Empirical Benchmark

The benchmark is implemented in `main.py`.

The script performs the following steps:

1. Generates random signals of increasing size.
2. Executes each algorithm on the signals.
3. Measures execution time.
4. Plots the empirical performance results.

Signal sizes used in the experiment:

n = 2⁰, 2¹, 2², ..., 2¹⁴

---

## Requirements

Python 3

Required libraries:

numpy  
matplotlib

Install dependencies:

pip install numpy matplotlib

---

## How to Run

Run the benchmark with:

python main.py

The program will generate a plot comparing the **empirical execution time** of each algorithm.

---

## Project Structure

.
├── main.py
├── DFT.py
├── DFT_REC.py
├── DFT_MAT.py
├── FFT_C.py
└── FFT_NUMPY.py

---

## Expected Results

The empirical results should illustrate that:

- DFT implementations scale approximately as **O(n²)**
- FFT implementations scale approximately as **O(n log n)**
- NumPy's FFT achieves the best performance due to its optimized low-level implementation.

---

## Educational Purpose

This project is intended for educational purposes in areas such as:

- Digital Signal Processing (DSP)
- Algorithm Analysis
- Numerical Computing

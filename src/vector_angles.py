#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    np.array([])

def main():
    X = np.array([[0, 0, 1], [-1, 1, 0]])
    Y = np.array([[0, 1, 0], [1, 1, 0]])
    angles = vector_angles(X, Y)
    print(f"Angles (degrees) between corresponding rows of\n{X}\nand\n{Y}:\n{angles}")

if __name__ == "__main__":
    main()

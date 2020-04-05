#!/usr/bin/env python3
 
from functools import reduce
import numpy as np
 
def matrix_power(a, n):
    if n >= 0:
        return reduce(np.matmul, (a for _ in range(n) ), np.eye(a.shape[0]))
    else:
        inv = np.linalg.inv(a)
        return reduce(np.matmul, (inv for _ in range(-n) ))
 
def main():
    a = np.array([[1,2], [3,4]])
    for n in range(-2,3):
        print(f"Power of {n}\n{matrix_power(a, n)}")
 
if __name__ == "__main__":
    main()
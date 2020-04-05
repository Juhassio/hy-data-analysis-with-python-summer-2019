#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    
    listaa = []
    
    for i in a:
        listaa.append(i)
    return listaa

def get_columns(a):
    
    listaa1 = []
    for i in a.T:
        listaa1.append(i)
    
    return listaa1

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()

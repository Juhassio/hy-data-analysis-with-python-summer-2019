#!/usr/bin/env python3
import pandas as pd

def read_series():
    arvot = []
    indeksit = []
    
    while True:
        data = input("Anna dataa: ")
        if len(data) == 0:
            break
        
        i, v = data.split()
        arvot.append(v)
        indeksit.append(i)
        
    s = pd.Series(arvot, index = indeksit)
    return s

    
"""        else:
            splittaus = data.split()
            if len(splittaus) > 2:
                raise Exception
                
            else:
                indeksit.append(splittaus[0])
                arvot.append(splittaus[1])
                #arvot.append("".join(splittaus[1:]))
    return pd.Series(arvot,indeksit)"""
    

def main():
    print(read_series())
    pass

if __name__ == "__main__":
    main()

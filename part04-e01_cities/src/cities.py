#!/usr/bin/env python3

import pandas as pd
import numpy as np

def cities():
    
    a=[[643272, 715.48],
       [279044, 528.03],
       [231853, 689.59],
       [223027, 240.35],
       [201810, 3817.52]]
    cols=["Population", "Total area"]
    ind=["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    df = pd.DataFrame(a, index=ind, columns=cols)
    return df
    
def main():
    df = cities()
    print(df.dtypes)
    print(df)
    
if __name__ == "__main__":
    main()
    


#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    
    df = pd.read_csv("municipal.tsv", sep ='\t', index_col = 0)
    return df["Akaa":"Äänekoski"]
    
    
    return None
    
def main():
    df=municipalities_of_finland()
    print(df.iloc[0,0])
    print(df.iloc[-1,-1])
    #df=pd.DataFrame()
    print("Shape: {}, {}".format(*df.shape))
    for name in df.columns:
        print(name)
    
if __name__ == "__main__":
    main()

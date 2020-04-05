#!/usr/bin/env python3

import pandas as pd

def below_zero():
    
    df =pd.read_csv("src/kumpula-weather-2017.csv")
    zero = df["Air temperature (degC)"] < 0]
    
    #print(len(zero))
    
    
    return len(zero)

def main():
    t = below_zero()
    print(f"Number of days below zero: {t}")
    return
    
if __name__ == "__main__":
    main()

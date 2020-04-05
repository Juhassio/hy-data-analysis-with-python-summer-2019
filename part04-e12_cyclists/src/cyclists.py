#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df2 =df.dropna(how ="all")
    df3 = df2.dropna(axis =1, how = "all")
    return df3


def main():
    tt = cyclists()
    print(tt)
    return
    
if __name__ == "__main__":
    main()

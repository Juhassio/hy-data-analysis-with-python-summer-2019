#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    wh = pd.read_csv("kumpula-weather-2017.csv")
    wh2 = wh.describe()["Snow depth (cm)"]["max"]
    return wh2

def main():
    maximum = snow_depth()
    
    print(f"Max snow depth: {maximum}")
    return

if __name__ == "__main__":
    main()

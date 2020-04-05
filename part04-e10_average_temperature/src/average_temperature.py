#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    wh = pd.read_csv("kumpula-weather-2017.csv")
    m = wh["m"]== 7
    wh2 = wh[m]["Air temperature (degC)"].mean()
    #wh2 = wh_july.describe().loc["mean", "Air temperature (degC)"]
    
    return wh2

def main():
    at = average_temperature()
    
    print(f"Average temperature in July: {at:.1f}")
    return

if __name__ == "__main__":
    main()

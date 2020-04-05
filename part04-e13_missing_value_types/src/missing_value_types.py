
import pandas as pd
import numpy as np

def missing_value_types():
    countries = ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia']
    year_of_inpedence = [, 1917, 1776,1523,,1992]
    presidents = [False, 'Niinistö', 'Trump', False, 'Steinmeier', 'Putin']
    
    df = pd.DataFrame({'State':countries, 'Year of independence':year_of_inpedence, 'President':presidents}).set_index('State')
    return df

def main():
    print(missing_value_types())
    
if __name__ == "__main__":
    main()

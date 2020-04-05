#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    indices = ['a','b','c']
    s1 = pd.Series(L1, indices)
    s2 = pd.Series(L2, indices)
    return (s1, s2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return (s1, s2)
    
def main():
    s1, s2 = create_series([2,3,4], [9,8,7])
    print("Original:")
    print(s1)
    print(s2)
    s1, s2 = modify_series(s1, s2)
    print("Modified:")
    print(s1)
    print(s2)
    print("Addition:")
    print(s1 + s2)
    print("""Note that the resulting type gets 
    converted to float to accomodate the missing value symbol NaN""")

if __name__ == "__main__":
    main()

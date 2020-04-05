#!/usr/bin/env python3


def merge(L1, L2):
   

    size_1 = len(L1) 
    size_2 = len(L2) 
  
    res = [] 
    i, j = 0, 0
  
    while i < size_1 and j < size_2: 
        if L1[i] < L2[j]: 
            res.append(L1[i]) 
            i += 1
  
        else: 
            res.append(L2[j]) 
            j += 1
  
    res = res + L1[i:] + L2[j:] 
    return res
    

def main():
    
    pass

if __name__ == "__main__":
    main()

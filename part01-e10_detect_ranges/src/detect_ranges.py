#!/usr/bin/env python3

def detect_ranges(L):
    a=sorted(L)
    l=[]
    
    maximum=a[0]-1
    for i in range(len(a)):
        d=a[i]
        e=d
        j=0
        for j in range(i, len(a)-1):
            if a[j+1] - a[j] == 1 :
                e=a[j+1]
                j=j+1
                i=j 
            else :
                i=j
                break
             
        if d < e  and d > maximum:
            l.append((d, e+1))
            maximum = e+1
        elif d> maximum :
            l.append(d)
                


    return l


def main():

    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)
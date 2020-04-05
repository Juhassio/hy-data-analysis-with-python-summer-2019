from statistics import stdev
import sys

def summary(filename):
    
    L = []
    with open(filename) as f:
        for line in f:
            try:
                L.append(float(line))
            except ValueError:
                continue
            
    s = sum(L)
    a = s/len(L)
    stddev = stdev(L)
    
    return s, a, stddev


def main():
    for filename in sys.argv[1:]:
        s,a,stddev = summary(filename)
        
    print(f"File: {filename} Sum: {s:.6f} Average: {a:.6f} Stddev: {stddev:.6f}")            
            
#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    
    
    
    d = (b**2) - (4*a*c)

    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    
    
    
    return ((sol1,sol2))
    


def main():
    pass

if __name__ == "__main__":
    main()

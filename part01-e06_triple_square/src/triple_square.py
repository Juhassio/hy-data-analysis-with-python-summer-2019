#!/usr/bin/env python3


def triple(x):
    return x*3

def square(y):
    return y**2

    pass


    
    
def main():
    for i in range(1,11):
        a=square(i)
        b=triple(i)
        if a>b:
           break
        print("triple({:d})=={:d} square({:d})=={:d}".format(i,b,i,a))

    
    
if __name__ == "__main__":
    main()
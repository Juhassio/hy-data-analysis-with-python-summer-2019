#!/usr/bin/env python3

def find_matching(L, pattern):
    list = []
    for a, b in enumerate(L):
        if(pattern in b): list.append(a)
    return list

def main():
    pass

if __name__ == "__main__":
    main()

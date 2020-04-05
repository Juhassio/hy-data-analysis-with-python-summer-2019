def interleave(*lists):
    
    l = []
    
    for t in zip(*lists):
        l.extend(t)
    return l    
    
    
   

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

def main():
    for i in range(1, 7):
        for j in range(1,7):
            k = i + j
            if(k == 5):
                print("({},{})".format(i, j))
                #print(i,j, end=' ')
        #print (' ')       
        
    #pass

if __name__ == "__main__":
    main()

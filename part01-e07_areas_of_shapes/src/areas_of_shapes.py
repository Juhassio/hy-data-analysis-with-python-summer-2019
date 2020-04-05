#!/usr/bin/env python3

import math


def main():
    areas = ["triangle, rectangle, circle"]
    
    
    
    while True:
        
        
        
        z = input("Choose a shape (triangle, rectangle, circle):")
        
        if z == "":
            break
    
        if z == "triangle":
            base = input("Give base of the triangle:")
            height = input("Give the height of the triangle:")
            area = int(base) * int(height)
            print("The area is", area/2)
            
        
        elif z == "rectangle":
            base = input("Give widht of the rectangle:")
            height = input("Give the height of the rectangle:")
            area = int(base) * int(height)
            print("The area is", area)
        
        elif z == "circle":
            base = input("Give radius of the circle:")
            #height = input("Give the height of the triangle:")
            area = int(base)**2 * math.pi
            print("The area is", area)
        
        elif z != areas: 
            print("Unknown shape!")
            
        
        
            
    
    

    # enter you solution here

if __name__ == "__main__":
    main()

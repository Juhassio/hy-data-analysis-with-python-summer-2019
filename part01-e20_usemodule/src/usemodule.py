#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    
    print(triangle.area(3, 4))
    print(triangle.hypothenuse(3, 4))
    print(triangle.__version__)
    # Call the functions from here

if __name__ == "__main__":
    main()

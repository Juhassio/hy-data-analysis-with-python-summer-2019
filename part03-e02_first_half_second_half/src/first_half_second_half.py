import numpy as np
 
def first_half_second_half(a):
    a1, a2 = np.split(a, 2, axis=1)
    mask = np.sum(a1, axis=1) > np.sum(a2, axis=1)
    return a[mask]
 
def main():
    m=4
    n=10
    np.random.seed(0)
    a = np.random.randn(n, 2*m)
    np.set_printoptions(linewidth=1000)
    print("a:\n", a)
    print("result:\n", first_half_second_half(a))
 
if __name__ == "__main__":
    main()
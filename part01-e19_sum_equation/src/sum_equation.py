def sum_equation(L):
    right_side = sum(L)
    str_list = [str(elem) for elem in L]
    left_side = ' + '.join(str_list) if len(L) else '0'
    return "{} = {}".format(left_side, right_side)

def main():
    print(sum_equation([1,5,7]))
    print(sum_equation([]))

    

if __name__ == "__main__":
    main()
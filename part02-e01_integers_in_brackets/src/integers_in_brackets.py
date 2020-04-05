#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    nums = re.findall(r"\[\s*([+-]?\d+)\s*\]",s)
    #nums = re.findall(r"\[[\s]*([+|-]{0,1}\d+)[\s]*\]", s)
    return list(map(int, nums))
    #return [int(num) for num  in nums]
    #return []

def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))
    print(integers_in_brackets(" afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xx"))

    pass

if __name__ == "__main__":
    main()

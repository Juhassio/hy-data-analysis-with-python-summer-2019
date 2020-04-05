#!/usr/bin/env python3

'''import sys
import os 
import re
import calendar


def process_line(line):
    months = "|".join(calendar.month_abbr[1:])
    parts = re.findall(r"hyad-all\s+(\d+)\s+(%s)\s+(\d+)\s+(\d{2}):(\d{2}) (.+)" % months, line)[0]
    
    return [int(part) if part.isdigit() else part for part in parts]

def read_lines(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + file_name, 'r')
    return f.readlines()

def file_listing():
    lines = read_lines('/listing.txt')
    return [process_line(line) for line in lines]

'''

import re

def file_listing(filename='src/listing.txt'):
    with open(filename) as f:
        lines = f.readlines()
    result = []
    for line in lines:
        pattern = r".{10}\s+\d+\s+.+\s+.+\s+(\d+)\s+(...)\s+(\d+)\s+(\d\d):(\d\d)\s+(.+)"
    if True :
        m =re.match(pattern,line)
    else:
        compiled_pattern = re.compile(pattern)
        m = compiled_pattern.match(line)
        if m: 
            t = m.groups()
            result.append((int(t[0]), t[1], int(t[2]), int(t[3]), int(t[4]), t[5]))
        else: 
            print(line)
            return result
    
    
    
def main():
    tuples = (file_listing())
    for t in tuples:
        print(t)
        
if __name__ == "__main__":
    main()

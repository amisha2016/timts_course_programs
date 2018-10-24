#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    p=s.split(' ')
    for i in range(0,len(p)):
        if (len(p[i])!=0):
            p[i]=p[i][0].upper()+p[i][1:]
    s=' '.join(p)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. Their absolute difference is |15-17|=2



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i == j):
                primary_diagonal += arr[i][j]
            if (i == len(arr[i])-1-j):
                secondary_diagonal += arr[i][j]

    return abs(primary_diagonal-secondary_diagonal)


#input:
arr = [
    [11, 2, 4], 
    [4, 5, 6], 
    [10, 8, -12]]
# Ouptut: 15

print(diagonalDifference(arr))
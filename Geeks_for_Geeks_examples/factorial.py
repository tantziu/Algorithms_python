import math

# You are given an array A of integers of length N. 
# You need to calculate factorial of each number. 
# The answer can be very large, so print it modulo 109 + 7.

# Input:
# N = 5
l1 = [0, 1, 2, 3, 4]
# Output:
# 1 1 2 6 24

# Input:
# N = 3
l2= [5, 6, 3]
# Output:
# 120 720 6
# Explanation:
# Factorial of 5 is 120, 
# factorial of 6 is 720, 
# factorial of 3 is 6.
def factorial(l):
    for i in range(len(l)):
        print(i)
        l[i] = math.factorial(i)
    return l


def factorial2(l):
    modulo = 1000000007
    maximum = max(l) + 1
    print(maximum)
    factorial_list = [1] * maximum

    for i in range(1, maximum):
        factorial_list[i] = (i * factorial_list[i-1])% modulo
    print(factorial_list)

    for i in range(len(l)):
        l[i] = factorial_list[l[i]]
    return l

print(factorial2(l2))
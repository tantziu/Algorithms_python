# Given an array A[] of n positive integers which can contain integers from 1 to n where 
# elements can be repeated or can be absent from the array. Your task is to count the 
# frequency of all elements from 1 to n.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

def frequency_count(a):
    d = {}
    result = len(a) * [0]
    for i in a:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    print(d) 

    for i in range(len(a)):
        if d.get(i+1):
            result[i] = d.get(i+1)
    a[:] = result
    print(a)


# a1 = [2,3,2,3,5]
# Output:
# 0 2 2 0 1

a2= [3,3,3,3]
# Output:
# 0 0 4 0
a3=[1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10]
# Output:
# Element 1 occurs 3 times
# Element 2 occurs 1 times
# Element 3 occurs 2 times
# Element 5 occurs 2 times
# Element 8 occurs 3 times
# Element 9 occurs 2 times
# Element 10 occurs 1 times
frequency_count(a3)


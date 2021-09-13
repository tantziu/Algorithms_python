def MissingNumber(array,n):
    array.sort()
    for i in range(0, n):
        if array[i] != i+1:
            return i+1

# n = 5
# array = [1,2,3,5]
# print(MissingNumber(array,n))
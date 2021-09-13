##################################
# Input:
n = 5 
d = 3
a = [1,2,3,4,5]
# Output: 3 4 5 1 2

# Input2:
# N = 10, D = 3
# arr = [2,4,6,8,10,12,14,16,18,20]
# Output: 8 10 12 14 16 18 20 2 4 6\

#Solution 1
def rotateArr(a, d, n):
    temp = []
    for i in range(n):
        if i < d:
            temp.append(a[i])
        if i<n-d:
            a[i] = a[i+d]

    for i in range(n-1, -1, -1):
        if i >= n-d:
            a[i] = temp.pop()
    return a

#Solution 2
def rotate_once_right(a):
    length = len(a)
    first = a[0]

    for i in range(length-1):
        a[i] = a[i+1]
            # print(a)
    a[length-1] = first

def rotateArr_2(a,d,n):
    for i in range(d):
        rotate_once_right(a)
    return a

#Solution 3, with %
def rotate_array_modulo(a,d,n):
    new_start = d
    start= 0
    #assuming the last element is max, or find max first
    offset = a[n-1]+1

    for i in range(n):
        if i<n-d:
            a[i]+= a[new_start] % offset * offset
            new_start += 1
        else:
            a[i]+= a[start] % offset * offset
            start += 1
    print(a)
    for i in range(n):
        a[i] = a[i] // offset
    print(a)

# rotate_once_right(a)
# print(rotateArr_2(a, d, n))
rotate_array_modulo(a,d,n)
# print(rotateArr(a, d, n))
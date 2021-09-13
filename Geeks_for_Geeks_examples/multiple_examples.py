import time
wowels = set(['a', 'e', 'i', 'o' , 'u', 'A', 'E', 'I', 'O', 'U'])

def wowel_reverse(input):
    wowels_in_input = []
    for x in input:
        if x in wowels:
            wowels_in_input.append(x)
    print(wowels_in_input)

    output = []
    for x in input:
        
        if x in wowels:
            output.append(wowels_in_input.pop())
        else:
            output.append(x)
    
    print("".join(output))

# wowel_reverse('enzo')
# wowel_reverse('ENZO')
# msg = 'hello'

def MissingNumber(array,n):
    array.sort()
    for i in range(0, n):
        if array[i] != i+1:
            return i+1

# n = 5
# array = [1,2,3,5]
# print(MissingNumber(array,n))


# start = time.time()
# time.sleep(1)
def trailingZeroes(N):
    fack = 1
    for i in range(1, N+1):
        fack *= i
    print(fack)
    
    no_remainder = True
    trailing = 0
    while no_remainder:
        if fack % 10 == 0:
            trailing += 1
            fack = fack // 10
        else:
            no_remainder = False
    print(trailing)
    return trailing
# trailingZeroes(10)


# end = time.time()
# print(f"Runtime of the program is {end - start}")
####################################################################
# n = 5
# a = [1,3,5,2,2]
def equilibriumPoint(a):
    left_sum = 0
    right_sum = 0
    for i in range(len(a)):
        # for j in a[i+1:]:
        #     right_sum += j
        right_sum = sum(a[i+1:])
        print("Right: ", right_sum)
        print("Left: ", left_sum)
        if left_sum == right_sum:
            return i+1
        else:
            left_sum += a[i]
            right_sum = 0

def equilibriumPoint_liniar(a):
    left_sum = 0
    right_sum = sum(a)

    for i in range(len(a)):
        mid_point = a[i]
        right_sum -= mid_point

        if left_sum == right_sum:
            return i+1
        else:
            left_sum += mid_point

# print(equilibriumPoint_liniar(a))
########################################################################
# a = [16,17,4,3,5,2]
def find_leaders(a):
    # right_sum = sum(a)
    maximum = 0
    leaders = []
    for i in a[::-1]:
        if i > maximum:
            maximum = i
            leaders.append(i)
    return leaders[::-1]

# print(find_leaders(a))

#########################################################################
# a = [3,2,3,7,5,2]
# s = 12

def sublist_sum(a, s):
    sequence_sum = 0
    beginning = 0
    for i in range(len(a)):
        sequence_sum += a[i]
        if sequence_sum == s:
            return f"{beginning} {i}"
        if sequence_sum > s:
            for j in range(beginning, i+1):
                sequence_sum = sequence_sum - a[j]
                beginning += 1
                if sequence_sum == s:
                    return f"{beginning} {i}"
                elif sequence_sum < s:
                    break
                    

# print(sublist_sum(a, s))

#############################################################################
# arr = [1,2,3,4,5,6]
# n = 6
 #expected: 6 1 5 2 4 3
#  6, max = 5
#
# 
def rearrange(arr, n):
    result = []
    min = 0
    max = n-1
    flag = True

    for i in range(n):
        if flag:
            result.append(arr[max])
            max -= 1            
        else:
            result.append(arr[min])
            min += 1
            
        flag = not flag
    return result

# print(rearrange(arr, n))

##################################
# Input:
n = 5 
d = 2
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
    new_start = d+1
    start= 0
    #assuming the last element is max, or fidn max first
    offset = a[n-1]+1

    for i in range(n):
        if i<n-d-1:
            a[i]+= a[new_start] % offset * offset
            new_start += 1
        else:
            a[i]+= a[start] % offset * offset
            start += 1

    for i in range(n):
        a[i] = a[i] // offset
    print(a)

# rotate_once_right(a)
# print(rotateArr_2(a, d, n))
rotate_array_modulo(a,d,n)

###########################################
def majority_element(a, n):
    half = n//2
    d = {}
    for i in range(n):
        if d.get(a[i]):
            d[a[i]] += 1
        else:
            d[a[i]] = 1
        if d[a[i]] == half+1:
            print(d)
            return a[i]
    return -1


# a = [1, 2, 9, 9, 9, 9]
# n = 6
# print(majority_element(a, n))
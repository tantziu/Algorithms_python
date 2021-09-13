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
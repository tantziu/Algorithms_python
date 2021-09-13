# Given an positive integer N and a list of N integers A[]. 
# Each element in the array denotes the maximum length of jump you can cover. 
# Find out if you can make it to the last index if you start at the first index of the list.

a1 = [1, 2, 0, 3, 0, 0]
# output 1
# Jump 1 step from first index to
# second index. Then jump 2 steps to reach 
# 4th index, and now jump 2 steps to reach
# the end.
a2 = [1, 0, 2]
a3 = [1]
# output 0

def can_reach(a):
    if len(a) < 0 or a[0] == 0:
        return 0
    
    maxReach = a[0]
    step = a[0]
    end = len(a) -1
    for i in range(1, len(a)):
        if i == len(a) - 1:
            return 1
        maxReach = max(maxReach, i + a[i])
        step -= 1
        if (i >= maxReach):
            return 0

        step = maxReach -i
    return 1

        # index += a[index]
        # print(index)
        # if index == end:
        #     return 1
        # elif index >= len(a) or a[index] == 0:
        #     return 0

print(can_reach(a1))
# Given a binary array arr of size N and an integer M. 
# Find the maximum number of consecutive 1's produced by flipping at most M 0's.
a1 = [1, 0, 1]
m1 = 1
# output:3
# 
a2 = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
m2 = 2
# output: 8

def find_zeroes(a, m):
    bestWindow = 0
    wLeft = wRight =0
    zeroCount = 0

    while wRight < len(a):
        if zeroCount <= m:
            if a[wRight] == 0:
                zeroCount += 1
            wRight += 1

        if zeroCount > m:
            if a[wLeft] == 0:
                zeroCount -= 1
            wLeft += 1

        if wRight-wLeft > bestWindow and zeroCount <= m:
            bestWindow = wRight - wLeft
    return bestWindow

print(find_zeroes(a2, m2))
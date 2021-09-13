from collections import deque

def rearrange(a):
    queue_positive = deque()
    queue_negative = deque()
    result = []
    for d in a:
        if d < 0:
            queue_negative.append(d)
        else:
            queue_positive.append(d)
    print(queue_positive)
    print(queue_negative)

    for i in range(len(a)):
        if i % 2 == 0:
            if len(queue_positive):
                result.append(queue_positive.popleft())
            else:
                if len(queue_negative):
                    result.append(queue_negative.popleft())
        else:
            if len(queue_negative):
                result.append(queue_negative.popleft())
            else:
                if len(queue_positive):
                    result.append(queue_positive.popleft())
    print(result)
# -------------------------------------------------------------------------
# solution too
def rearrange2(a):
    out_of_place = -1

    for i in range(len(a)):
        if out_of_place >= 0:
            if a[i] >= 0 and a[out_of_place] < 0 or a[i] < 0 and a[out_of_place] >= 0:
                a = rotate_once_right(a, out_of_place, i)
                if i - out_of_place > 2:
                    out_of_place += 2
                else:
                    out_of_place = -1
        if out_of_place == -1:
            if a[i] >= 0 and i % 2 == 1 or a[i] < 0 and i % 2 == 0:
                out_of_place = i 
                # out_of_place = 1, i = 2
        
    return a

def rotate_once_right(a, out_of_place, current):
    first = a[current]

    for i in range(current, out_of_place, -1):
        a[i] = a[i-1]
    a[out_of_place] = first
    return a


a1 = [9, 4, -2, -1, 5, 0, -5, -3, 2]
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
a2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0 

print(rearrange2(a2))
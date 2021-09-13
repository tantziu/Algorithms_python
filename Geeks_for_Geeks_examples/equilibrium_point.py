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
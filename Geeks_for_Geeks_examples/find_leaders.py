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
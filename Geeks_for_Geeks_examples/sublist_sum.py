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
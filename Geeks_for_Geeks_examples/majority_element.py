
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
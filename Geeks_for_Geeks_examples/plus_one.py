def plus_one(a, n):
    a[n-1] += 1
    carry = a[n-1] // 10
    a[n-1] = a[n-1] % 10

    for i in range(n-2, -1, -1):
        if carry == 1:
            a[i] += 1
            carry = a[i] // 10
            a[i] = a[i] % 10

    if carry == 1:
        a.insert(0, 1)
    return a


a = [0, 9, 9, 9, 9]
n = 5
print(plus_one(a, n))
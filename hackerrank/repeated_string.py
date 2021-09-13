def repeated_string(s, n):
    if not len(s):
        return 0
    if len(s) == 1 and s =='a':
        return n
    
    return n // len(s) * s.count('a') + s[:n % len(s)].count('a')


# expected = 4
s1 = 'abcac'
n1 = 10

# expected = 7
s2 = 'aba'
n2 = 10


# expected = 1000000000000
s3 = 'a'
n3 = 1000000000000


print(repeated_string(s3, n3))
def strStr(haystack: str, needle: str) -> int:
    l1 = len(haystack)
    l2 = len(needle)
    if l2 == 0:
        return 0
    if  needle not in haystack:
        return -1
    
    for s in range(l1-l2+1):
        n = 0
        while n < l2:
            if haystack[s+n] != needle[n]:
                break
            n += 1
        if n == l2:
            return s


haystack1 = "hello"
needle1 = "ll"
# Output: 2

haystack2 = "aaaaa"
needle2 = "bba"
# Output: -1

haystack3 = ""
needle3 = ""
# Output: 0

haystack3 = "abc"
needle3 = "c"
# Output: 2

print(strStr(haystack2, needle2))
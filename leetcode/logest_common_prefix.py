# Example 1:

# Input: 
strs1 = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: 
strs2 = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
def longest_common_prefix(a):
    prefix = ""
    print(a)
    for i in range(len(a[0])):
        if a[0][i] == a[-1][i]:
            prefix += a[0][i]
        else:
            break
    return prefix


print(longest_common_prefix(strs2))
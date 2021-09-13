# Example 1:

# Input: 
s = ["h","e","l","l","o"]
s2 = []
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverse_string(s):
    for i in range(len(s)//2):
        temp = s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = temp
    print(s)

reverse_string(s2)
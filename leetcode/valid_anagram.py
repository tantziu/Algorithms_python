# Example 1:

# Input: 
# s = "anagram"
# t = "nagaram"
# Output: true
# Example 2:

# Input: 
s = "rat"
t = "car"
# Output: false

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    string1 = sorted(s)
    string2 = sorted(t)

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    return True


print(is_anagram(s, t))
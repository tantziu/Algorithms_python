def first_uniq_char(s: str) -> int:
    dictionary = {}
    for ch in s:
        if dictionary.get(ch):
            dictionary[ch] += 1
        else:
            dictionary[ch] = 1
    # print(dictionary)

    for key in dictionary:
        if dictionary[key] == 1:
            for i in range(len(s)):
                if s[i] == key:
                    return i
    return -1

s1 = "leetcode"
# return 0.

s2 = "loveleetcode"
# return 2.

s3 = "lllll"
print(first_uniq_char(s3))

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         """
#         :type s: str
#         :rtype: int
#         """
#         # build hash map : character and how often it appears
#         count = collections.Counter(s)
        
#         # find the index
#         for idx, ch in enumerate(s):
#             if count[ch] == 1:
#                 return idx     
#         return -1
# Example 1:

# Input: 
# x = 123
# Output: 321
# Example 2:

# Input: 
x = -123
# Output: -321
# Example 3:

# Input: 
# x = 120
# Output: 21
# Example 4:

# Input: 
# x = 0
# Output: 0

def reverse(x: int):
    if x == 0:
        return 0

    lowest = - pow(2, 31)
    greatest = pow(2, 31) - 1
    negative = x < 0
    integers = []
    x = abs(x)
    while x / 10 > 0:
        integers.append(x % 10)
        x = x // 10

    # n = ""
    # for integer in s:
    #     n += str(integer)
    strings = [str(i) for i in integers]
    result_string = ""
    if negative:
        result_string = "-"
    result_string += "".join(strings) 
    result_integer = int(result_string)

    if result_integer < lowest or result_integer > greatest:
        return 0
    return result_integer


print(reverse(x))

# Java Solution
# class Solution {
#     public int reverse(int x) {
#         int rev = 0;
#         while (x != 0) {
#             int pop = x % 10;
#             x /= 10;
#             if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
#             if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
#             rev = rev * 10 + pop;
#         }
#         return rev;
#     }
# }
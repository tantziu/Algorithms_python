def string_rotation(first, second):
    duplicate = second + second
    return is_substring(first, duplicate)

def is_substring(first, second):
    if first in second or second in first:
        return True
    return False


print(string_rotation("waterbottle", "erbottlewat"))
# print(is_substring("tania", "ana"))

def one_away(string1, string2):
    if string1 == string2:
        return False
    if len(string1) == len(string2):
        return check_replace(string1, string2)

    elif abs(len(string1) - len(string2)) == 1:
        return check_add_remove(string1, string2)

    return False


def check_replace(string1, string2):
    difference = False
    for i, j in zip(string1, string2):
        if i != j:
            if difference:
                return False
            difference = True

            #if not difference:
            #   difference = True
            #else:
            #    return False
    return True


def check_add_remove(string1, string2):
    if len(string1) > len(string2):
        longest, shortest = string1, string2
    else:
        longest = string2
        shortest = string1

    for i in range(len(shortest)):
        if shortest[i] != longest[i]:
            if shortest[i:] == longest[i+1:]:
                return True
            return False
    return True


#print(check_replace("pale", "palm"))
print(one_away("pal", "pale"))

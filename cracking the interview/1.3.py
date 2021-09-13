#Example:
#Input: "Mr John Smith    ", 13
#Output: "Mr%20John%20Smith"
#13 - length of string


def urlify(string, length):
    cut_string = string[:length]
    result = cut_string.replace(" ", "%20")
    return result


#print(urlify("Mr John Smith    ", 13))

def urlify_count_spaces(string, length):
    strip_string = string.rstrip()

    result = []
    index = 0
    for i in range(0, len(strip_string)):
        if strip_string[i] == " ":
            result.append("%20")
            index += 3
        else:
            result.append(strip_string[i])
            index += 1

    return ''.join(result)


print(urlify_count_spaces("Mr John Smith    ", 13))

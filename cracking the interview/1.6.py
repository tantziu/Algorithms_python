def string_compression(string):
    result = []
    count = 0

    for i in range(len(string)):
        count += 1

        if (i < len(string) - 1 and string[i] != string[i+1]) or i == len(string) - 1:
            result.append(string[i] + str(count))
            count = 0
    if len(''.join(result)) > len(string):
        return string
    return ''.join(result)


print(string_compression('aabcccccaaa'))

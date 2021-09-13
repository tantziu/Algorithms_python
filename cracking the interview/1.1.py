def has_unique_characters(some_string):
    if len(some_string) > 128:
        print("false")

    char_set = [False] * 128
    for i in range(0, len(some_string)):
        val = ord(some_string[i])
        if char_set[val]:
            print("Already found this {} char in string".format(chr(val)))
            return False
        char_set[val] = True
    print("All characters are unique")
    return True


# has_unique_characters("tatiana")


def has_unique_characters_bit_vector(some_string):
    #An integer to store presence/absence
    # of 26 characters using its 32 bits
    checker = 0
    for i in range(0, len(some_string)):
        val = ord(some_string[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            print('false')
            return False
        #set bit in checker
        checker = checker | (1 << val)
    print("true")
    return True


#has_unique_characters_bit_vector("mihai")

#compare every character with other character
def has_unique_characters_compare(string):
    character = 0
    for i in range(0, len(string)):
        for j in range(i, len(string)-1):
            if string[character] == string[j+1]:
                print("Characters are not unique")
                return
        character += 1
    print("All characters are unique")
#has_unique_characters_compare('sdfg')


#sort and check if neihgbours are identical
def has_unique_characters_sort(string):
    result = ''.join(sorted(string))
    print(result)
    for i in range(0, len(result)-1):
        #if (result[i] == result[i-1]) or (result[i] == result[i+1]):
        if ord(result[i]) - ord(result[i+1]) == 0:
            print("Ups!! Repeating letters")
            return
    print('No Repetition')


has_unique_characters_sort('mihai')

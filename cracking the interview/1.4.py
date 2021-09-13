def is_palindrome_permutation(string):
    words = string.replace(" ", "").lower()

    letters = {}
    for i in words:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 0
    print(letters)

    count = 0
    for l in letters:
        if letters[l] == 0:
            count += 1
    #if even
    if len(words) % 2 == 0:
        if count == 0:
            print("Palindrome Permutation! Yay!")
        else:
            print("Nope")
    else:
        if count == 1:
            print("Palindrome Permutation! Yay!")
        else:
            print("Nope")


#is_palindrome_permutation("Tact Coa")
#is_palindrome_permutation("bbaaaaa")

def palindrome_bit_vector(string):
    words = string.replace(" ", "").lower()
    cheker = 0

    for char in words:
        index = ord(char) - ord('a')
        mask = 1 << index
        cheker = cheker ^ mask

    if len(words) % 2 == 0:
        if cheker == 0:
            return True
        return False
    else:
        counter = 0
        for i in range(26):
            if (1 << i) & cheker:
                counter += 1
        if counter == 1:
            return True
        return False
    #print(bin(cheker))


print(palindrome_bit_vector("Tact Coa"))
print(palindrome_bit_vector("aabbac"))

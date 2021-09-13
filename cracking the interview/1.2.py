def check_permutations(string1, string2):
    if len(string1) != len(string2):
        return
    sort1 = ''.join(sorted(string1))
    sort2 = ''.join(sorted(string2))
    print(sort1)
    print(sort2)
    # for i in range(0, n1, 1):  to compare strings
    if sort1 == sort2:
        print("Yay, permutations")


#check_permutations('abcd', 'cadb')


#count how many times each letter and store in 2 arrays, then compare them
def check_permutations_with_arrays(string1, string2):
    if len(string1) != len(string2):
        return

    list1 = create_list_of_characters_count(string1)
    list2 = create_list_of_characters_count(string2)

    if list1 == list2:
        print("Permutations detected")
        return
    print("No permutations")


def create_list_of_characters_count(string):
    count_list = [0] * 128
    for i in range(0, len(string)):
        character = ord(string[i])
        count_list[character] += 1
    return count_list


check_permutations_with_arrays("tania", "aniat")

vowels = set(['a', 'e', 'i', 'o' , 'u', 'A', 'E', 'I', 'O', 'U'])

def vowel_reverse(input):
    wowels_in_input = []
    for x in input:
        if x in vowels:
            wowels_in_input.append(x)
    print(wowels_in_input)

    output = []
    for x in input:
        
        if x in vowels:
            output.append(wowels_in_input.pop())
        else:
            output.append(x)
    
    print("".join(output))

# vowel_reverse('enzo')
# vowel_reverse('ENZO')
# msg = 'hello'
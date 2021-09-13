def fun_with_agaram(text):
    for i in range(len(text)):
        for j in range(len(text)-1, i, -1):
            if sorted(text[i]) == sorted(text[j]):
                del text[j]

    return text
        



input = ['code', 'doce', 'ecod', 'framer', 'frame']
print(fun_with_agaram(input))
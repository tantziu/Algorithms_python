def fun_with_agaram(text):
    # result = [text[0]]
    # deleted
    # current = result[0]
    # for el in range(1, len(text)):
    #     if sorted(current) != sorted(text[el]):
    #         result.append(text[el])
    #     else:


    #     print(text[el])
    for i in range(len(text)):
        for j in range(len(text)-1, i, -1):
            if sorted(text[i]) == sorted(text[j]):
                del text[j]

    return text
        



input = ['code', 'doce', 'ecod', 'framer', 'frame']
print(fun_with_agaram(input))
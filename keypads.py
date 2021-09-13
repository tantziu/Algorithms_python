def make_search_dict(keypad):
    # So smart, very AI
    d = {}
    d[keypad[0]] = {keypad[1], keypad[3], keypad[4]}
    d[keypad[1]] = {keypad[0], keypad[2], keypad[3], keypad[4], keypad[5]}
    d[keypad[2]] = {keypad[1], keypad[4], keypad[5]}
    d[keypad[3]] = {keypad[0], keypad[1], keypad[4], keypad[6], keypad[7]}
    d[keypad[4]] = {keypad[0], keypad[1], keypad[2], keypad[3], keypad[5], keypad[6], keypad[7], keypad[8]}
    d[keypad[5]] = {keypad[1], keypad[2], keypad[4], keypad[7], keypad[8]}
    d[keypad[6]] = {keypad[3], keypad[4], keypad[7]}
    d[keypad[7]] = {keypad[3], keypad[4], keypad[5], keypad[6], keypad[8]}
    d[keypad[8]] = {keypad[4], keypad[5], keypad[7]}
    return d


def entryTime(s, keypad):
    if not s:
        return 0
        
    search_dict = make_search_dict(keypad)

    prev = s[0]
    time = 0
    for i in range(1, len(s)):
        if prev == s[i]:
            continue
        elif s[i] in search_dict[prev]:
            time += 1
        else:
            time += 2
        prev = s[i]

    return time


print(entryTime('5111', '752961348'))
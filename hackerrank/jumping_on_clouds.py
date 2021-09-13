def jumping_on_clouds(c):
    # current_position = None
    nr_jumps = 0 
    i = 0

    while i < len(c)-2:
        if c[i+2] == 0:
            i += 2
        else:
            i += 1
        nr_jumps +=1

    if i == len(c)-2:
        nr_jumps += 1

    return nr_jumps
            

    # return min(results)

# expect to return 3
input1 = [0, 1, 0, 0, 0, 1, 0]

# expect to return 4
input2 = [0, 0, 1, 0, 0, 1, 0]

# expect 3
input3= [0, 0, 0, 1, 0, 0]

print(jumping_on_clouds(input1))
def find_doubles_in_list(input_list):
    result = []
    # double = 0
    for item in input_list:
        double = 2 * item

        count = 0
        for value in input_list:
            if double == value:
                count += 1
        if count == 1:
            result.append(item)

    if result:
        return sorted(result)
    return None


    # return result
    

input1 = [1,2,3,4,5,6,7,8,9,0,8]
input2 = [7,17,11,1,23]
input3 = [1,1,2]

print(find_doubles_in_list(input))
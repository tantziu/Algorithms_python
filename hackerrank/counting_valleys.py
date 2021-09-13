
def counting_valleys(path):
    valleys = 0
    level = 0
    in_valley = False

    for ch in path:
        if ch == 'D':
            level -= 1
            if level == 0:
                in_valley = False
            if level < 0 and not in_valley:
                valleys +=1
                in_valley = True

            
        if ch == 'U':
            level += 1

            if level == 0:
                in_valley = False
            if level < 0 and not in_valley:
                valleys +=1
                in_valley = True
  
    return valleys

# expect 1
input1 = 'UDDDUDUU'
# expect 1
input2 = 'DDUUUUDD'
# expected 2
input3= 'DDUUDDUDUUUD' 
print(counting_valleys(input1))
import time

# start = time.time()
# time.sleep(1)
def trailingZeroes(N):
    fack = 1
    for i in range(1, N+1):
        fack *= i
    print(fack)
    
    no_remainder = True
    trailing = 0
    while no_remainder:
        if fack % 10 == 0:
            trailing += 1
            fack = fack // 10
        else:
            no_remainder = False
    print(trailing)
    return trailing
# trailingZeroes(10)


# end = time.time()
# print(f"Runtime of the program is {end - start}")
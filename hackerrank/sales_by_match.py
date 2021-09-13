from collections import defaultdict

def sock_merchant(arr):
    socks_dict = defaultdict()

    for el in arr:
        # if el not in socks_dict:
        #     socks_dict[el] = 1
        # else:
        #     socks_dict[el] += 1
        socks_dict[el] += 1

    pair_socks = 0
    for color in socks_dict:
        pair_socks += socks_dict[color] // 2

    return pair_socks

input =  [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sock_merchant(input))
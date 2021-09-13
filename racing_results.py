import collections

def racing_results(db):
    points_dict = {1:10, 2:6, 3:4, 4:3, 5:2, 6:1}
    racer_dict = {}

    
    for line in db:
        racer = line[1]
        key = line[2]
        points = 0

        if key in points_dict:
            points = points_dict[key]

        if racer in racer_dict: 
            racer_dict[racer] += points
        else:
            racer_dict[racer] = points


    ordered_dict = collections.OrderedDict(sorted(racer_dict.items()))
    # racer_dict = dict(sorted(racer_dict.items()))
    get_winner(ordered_dict)
    get_relegated(ordered_dict)


def get_winner(racer_dict):
    values = racer_dict.values()
    max_value = max(values)

    print()
    for key, value in racer_dict.items():
        if value == max_value:
            print(key, value)

def get_relegated(racer_dict):
    result = []
    for key in racer_dict:
        if racer_dict[key] == 0:
            result.append(key)
    print(' '.join(map(str, result)))


# def initialize_matrix(w, h):
#     return [[0]*w for i in range(h)]


# def populate_matrix(m, db):
#     for line in db:
#         # print("line", line)
#         i = line[0] % 2000
#         j = line[1] % 1000
#         # print('m[',i-1,'],[', j-1, ']=', line[2])
#         m[i-1][j-1] = line[2]
#     return m

# def compute_points(m, racer_dict):
#     for place in range(len(m)):
#         print

# def print_matrix(m):
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             print(m[i][j])

input = [
    [2001, 1002, 2],
    [2001, 1001, 3],
    [2002, 1003, 1],
    [2002, 1001, 2],
    [2002, 1002, 3],
    [2001, 1003, 1]
]

input2 = [
    [2002, 1003, 1],
    [2001, 1001, 3],
    [2001, 1002, 2],
    [2002, 1001, 2],
    [2002, 1002, 1],
    [2001, 1003, 2],
    [2001, 1004, 7],
    [2002, 1004, 8]
]

racing_results(input2)
# get_winner({1: 20, 2: 15, 3: 10, 4:20})


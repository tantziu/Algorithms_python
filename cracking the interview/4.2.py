from classes.tree import Node


def minimal_tree(sorted_list):
    middle = len(sorted_list) // 2
    root = Node(sorted_list[middle])
    left = sorted_list[:middle]
    right = sorted_list[middle+1:]
    if left:
        root.left = minimal_tree(left)
    if right:
        root.right = minimal_tree(right)
    return root


if __name__ == '__main__':
    print(minimal_tree([2, 3, 4, 5, 7, 8, 9, 10]))


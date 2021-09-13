from classes.tree import Node


def balanced_binary_tree(node):
    left_branch = get_height(node.left)
    right_branch = get_height(node.right)

    if abs(left_branch - right_branch) <= 1:
        return True
    return False


def get_height(node):
    if node is None:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1


if __name__ == '__main__':
    tree = {
        '1': ['2', '3'],
        '2': ['4', '5'],
        '3': ['6'],
        '5': ['7'],
    }
    root = Node('1')
    root.left = Node('2')
    root.right = Node('3')
    root.left.left = Node('4')
    root.left.right = Node('5')
    # root.right.left = Node('6')
    root.left.right.right = Node('7')
    print(balanced_binary_tree(root))
    # print(get_height(root))

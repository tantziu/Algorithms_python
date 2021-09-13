from classes.node import SLinkedList
from classes.node import Node


def list_of_depths(tree, node):
    levels_list = [[node]]

    for level in levels_list:
        storage = []
        for element in level:
            if element in tree.keys():
                for neighbour in tree[element]:
                    storage.append(neighbour)
        if storage:
            levels_list.append(storage)

    return levels_list


def list_of_depths2(tree, node):
    levels_list = [[node]]

    current_level = levels_list[0]
    while current_level:
        next_level = []
        for element in current_level:
            if element in tree.keys():
                for neighbour in tree[element]:
                    next_level.append(neighbour)

        current_level = next_level
        if next_level:
            levels_list.append(next_level)

    return levels_list


def linked_list_of_depths(tree, node):
    linked_list = SLinkedList()
    linked_list.head = Node(node)
    levels_list = [linked_list]
    current_level = levels_list[0]
    while current_level.head:
        next_level = SLinkedList()
        head = current_level.head
        while head:
            if head.data in tree.keys():
                for neighbour in tree[head.data]:
                    next_level.insert_at_the_end(neighbour)
            head = head.next
        current_level = next_level
        if next_level.head:
            levels_list.append(next_level)

    return levels_list


if __name__ == '__main__':
    tree = {
        '1': ['2', '3'],
        '2': ['4', '5'],
        '3': ['6'],
        '5': ['7'],
    }
    print(linked_list_of_depths(tree, '1'))


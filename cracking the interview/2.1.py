from classes.node import SLinkedList
from classes.node import Node


def remove_duplicates(a_list):
    dictionary = {}
    node = a_list.head

    while node:
        if node.data in dictionary:
            dictionary[node.data] += 1
        else:
            dictionary[node.data] = 0
        node = node.next
    print(dictionary)

    for key in dictionary:
        while dictionary[key] != 0:
            remove_node(key, a_list.head)
            dictionary[key] -= 1
            print(dictionary)
    return node


def remove_duplicates_in_one_traversal(a_list):
    node = a_list.head
    dictionary = {node.data}

    while node.next:
        if node.next.data in dictionary:
            node.next = node.next.next
        else:
            dictionary.add(node.data)
            node = node.next


def remove_node(key, head):
    if head.data == key:
        return head.next

    prev = head
    node = head.next
    while node:
        if node.data == key:
            prev.next = node.next
            node = node.next
            break

        prev = node
        node = node.next

    return head


def remove_duplicates_without_data_structure(a_list):
    probe = a_list.head
    current = a_list.head
    while probe:
        while current.next:
            if probe.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        current = probe.next
        probe = current


a_list = SLinkedList()
a_list.head = Node("Mon")
e2 = Node("Tue")
a_list.head.next = e2
e3 = Node("Wed")
e2.next = e3
e4 = Node("Thu")
e3.next = e4
e5 = Node("Tue")
e4.next = e5
e6 = Node("Tue")
e5.next = e6

# remove_duplicates(a_list)
# print(a_list)
# remove_duplicates_without_data_structure(a_list)
# print(a_list)

#in one method
print(a_list)
remove_duplicates_in_one_traversal(a_list)
print(a_list)

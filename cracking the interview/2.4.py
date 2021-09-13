from classes.node import SLinkedList
from classes.node import Node


def partition(linked_list, k):
    left_part = SLinkedList()
    right_part = SLinkedList()

    node = linked_list.head
    while node:
        next_node = node.next
        if node.data < k:
            add_to_list(left_part, node)
        else:
            add_to_list(right_part, node)
        node = next_node

    last = left_part.head
    while last.next:
        last = last.next
    last.next = right_part.head
    return last.next


def add_to_list(linked_list, node):
    node.next = None
    if linked_list.head is None:
        linked_list.head = node
        return

    last = linked_list.head
    while last.next:
        last = last.next
    last.next = node


def partition_faster(linked_list, k):
    head = linked_list.head
    tail = head
    current = head
    while current:
        next = current.next
        if current.data < k:
            #insert node at head:
            current.next = head
            head = current
        else:
            #insert at tail
            tail.next = current
            tail = current
        current = next
    tail.next = None
    linked_list.head = head


linked_list = SLinkedList()
linked_list.head = Node(3)
e2 = Node(5)
linked_list.head.next = e2
e3 = Node(8)
e2.next = e3
e4 = Node(5)
e3.next = e4
e5 = Node(10)
e4.next = e5
e6 = Node(2)
e5.next = e6
e7 = Node(1)
e6.next = e7

print(linked_list)
# partition(linked_list, 5)
# print(linked_list)
# some_list = SLinkedList()
# add_to_list(some_list, 1)
# print(some_list)
partition_faster(linked_list, 5)
# linked_list.list_print()
print(linked_list)

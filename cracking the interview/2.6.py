from classes.node import SLinkedList
from classes.node import Node


def is_palindrome(linked_list):
    reversed_list = reverse_list(linked_list)

    head_linked_list = linked_list.head
    head_reversed_list = reversed_list.head

    while head_linked_list:
        if head_linked_list.data != head_reversed_list.data:
            return False
        head_linked_list = head_linked_list.next
        head_reversed_list = head_reversed_list.next
    return True


def reverse_list(linked_list):
    mirror_list = SLinkedList()
    head = linked_list.head
    while head:
        head_next = head.next
        head.next = None
        if mirror_list.head is None:
            mirror_list.head = head
        else:
            new_node = head
            new_node.next = mirror_list.head
            mirror_list.head = new_node
        head = head_next
    return mirror_list


linked_list = SLinkedList()
linked_list.head = Node('a')
e2 = Node('b')
linked_list.head.next = e2
e3 = Node('c')
e2.next = e3
e4 = Node('d')
e3.next = e4
e5 = Node('c')
e4.next = e5
e6 = Node('b')
e5.next = e6
e7 = Node('a')
e6.next = e7

print(linked_list)
print(is_palindrome(linked_list))

from classes.node import SLinkedList
from classes.node import Node


def delete_middle_node(middle):
    next_node = middle.next

    middle.data = next_node.data
    middle.next = next_node.next


linked_list = SLinkedList()
linked_list.head = Node("Mon")
e2 = Node("Tue")
linked_list.head.next = e2
e3 = Node("Wed")
e2.next = e3
e4 = Node("Thu")
e3.next = e4
e5 = Node("Fri")
e4.next = e5
e6 = Node("Sat")
e5.next = e6

print(linked_list)
delete_middle_node(e4)
print(linked_list)

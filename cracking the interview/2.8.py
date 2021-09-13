from classes.node import SLinkedList
from classes.node import Node


def loop_detection(head):
    node_set = set()
    while head:
        if head in node_set:
            return head
        node_set.add(head)
        head = head.next

link = SLinkedList()
link.head = Node(7)
e2 = Node(1)
link.head.next = e2
e3 = Node(6)
e2.next = e3
e6 = Node(9)
e3.next = e6
e4 = Node(4)
e6.next = e4
e4.next = e3


print(loop_detection(link.head).data)

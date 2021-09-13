from classes.node import SLinkedList
from classes.node import Node
from classes import node


list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link first node to second node:
list1.head.next = e2
e2.next = e3

#Treversing the list:
#list1.list_print()

#insert at the beginning
list1.insert_at_the_beginning("Sun")
#list1.list_print()

#insert at the end:
list1.insert_at_the_end("Thu")
# list1.list_print()

#insert in between:
list1.insert_in_between(list1.head.next, "Fri")
# list1.list_print()

#remove node
list1.remove_node("Fri")
# list1.head = node.remove_node(list1.head, "Fri")
list1.list_print()


from classes.node import SLinkedList
from classes.node import Node


def return_key_to_last(linked_list, key):
    current = linked_list.head
    while current:
        if current.data == key:
            linked_list.head = current
            return
        else:
            current = current.next


def return_kth_to_last(linked_list, k):
    head = linked_list.head
    counter = 0
    while head:
        counter += 1
        head = head.next
    # print(counter)

    node = linked_list.head
    index = counter - k
    if index < 0:
        print("The length of linked list is smaller than your k!")
        return

    position = 0
    while node:
        if index == position:
            # print(index)
            # print(node.data)
            linked_list.head = node
            return
        node = node.next
        position += 1


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

# remove_duplicates(a_list)
print(linked_list)
# return_key_to_last(linked_list, "Thu")
return_kth_to_last(linked_list, 7)
print(linked_list)

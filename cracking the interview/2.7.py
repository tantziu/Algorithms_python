from classes.node import SLinkedList
from classes.node import Node


class Result:
    def __init__(self, length, tail):
        self.length = length
        self.tail = tail


def get_tail_and_length(node):
    count = 1
    current = node
    while current.next:
        count += 1
        current = current.next
    return Result(count, current)


def advance_pointer_for_longer(node, pointer):
    count = 0
    current = node
    while current:
        if count == pointer:
            return current
        count += 1
        current = current.next


def intersecting_node(first, second):
    result1 = get_tail_and_length(first)
    result2 = get_tail_and_length(second)
    #if different tails, no intersection
    if result1.tail != result2.tail:
        return

    shorter = first if result1.length < result2.length else second
    longer =  first if result1.length > result2.length else second

    longer = advance_pointer_for_longer(longer, abs(result1.length - result2.length))
    while longer != shorter:
        longer = longer.next
        shorter = shorter.next

    return longer


first = SLinkedList()
first.head = Node(7)
e2 = Node(1)
first.head.next = e2
e3 = Node(6)
e2.next = e3
e6 = Node(9)
e3.next = e6

second = SLinkedList()
second.head = Node(5)
# e4 = Node(9)
e4 = e3
second.head.next = e4
e5 = Node(4)
e4.next = e5
print("Input:")
print(first)
print(second)
print("Result:")
print(intersecting_node(first.head, second.head).data)


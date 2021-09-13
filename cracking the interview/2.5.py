from classes.node import SLinkedList
from classes.node import Node


def sum_lists(first, second):
    # reverse_first = reverse_list(first)
    # reverse_second = reverse_list(second)
    # print(reverse_first)
    # print(reverse_second)
    # first_head = reverse_first.head
    # second_head = reverse_second.head
    first_head = first.head
    second_head = second.head

    result = SLinkedList()
    memory = 0
    while first_head or second_head:
        if first_head and second_head:
            total = first_head.data + second_head.data + memory
            if total / 10 > 1:
                memory = 1
                append_to_list(result, total % 10)
            else:
                memory = 0
                append_to_list(result, total)
            first_head = first_head.next
            second_head = second_head.next
        else:
            if second_head is None:
                total = first_head.data + memory
                append_to_list(result, total % 10)
                first_head = first_head.next
            elif first_head is None:
                total = second_head.data + memory
                append_to_list(result, total % 10)
                second_head = second_head.next
            else:
                return

    if memory == 1:
        append_to_list(result, 1)

    return result


def append_to_list(linked_list, data):
    node = Node(data)
    if linked_list.head is None:
        linked_list.head = node
        return

    last = linked_list.head
    while last.next:
        last = last.next
    last.next = node


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


def sum_lists_recursive(first, second, carry):
    first_data = 0 if not first else first.data
    second_data = second.data if second else 0

    total = first_data + second_data + carry
    carry = total // 10
    result = Node(total % 10)
    if first or second:
        result.next = sum_lists_recursive(first.next if first else None, second.next if second else None, carry)
    return result


def print_recursive(node):
    print(node.data)
    if node.next:
        print_recursive(node.next)


def copy_recursive(node):
    new_node = Node(node.data)
    if node.next:
        new_node.next = copy_recursive(node.next)
    return new_node


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
e4 = Node(9)
second.head.next = e4
e5 = Node(4)
e4.next = e5
print("Input:")
print(first)
print(second)
print("Result:")
# print(sum_lists(first, second))


print_recursive(sum_lists_recursive(first.head, second.head, 0))
# print_recursive(copy_recursive(first.head))

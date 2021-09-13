class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        curr = self.head
        out = []
        while curr:
            out.append(str(curr.data))
            curr = curr.next
        return " -> ".join(out)

    def list_print(self):
        print_value = self.head
        while print_value is not None:
            print(print_value.data)
            print_value = print_value.next

    def insert_at_the_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_the_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_in_between(self, middle_node, new_data):
        if middle_node is None:
            print("No specified node to insert after")
            return
        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node

    def remove_node(self, key):
        if self.head.data == key:
            self.head = self.head.next
            return

        previous = self.head
        node = self.head.next
        while node:
            if node.data == key:
                previous.next = node.next
                node = node.next
                continue

            previous = node
            node = node.next


def remove_node(head, key):
    if head.data == key:
        return head.next

    prev = head
    node = head.next
    while node:
        if node.data == key:
            prev.next = node.next
            node = node.next
            continue

        prev = node
        node = node.next

    return head

from classes.stack import Stack


def sort_stack(unsorted_stack):
    sorted_stack = Stack()
    while not unsorted_stack.is_empty():
        temp = unsorted_stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            unsorted_stack.push(sorted_stack.pop())
        sorted_stack.push(temp)

    while not sorted_stack.is_empty():
        unsorted_stack.push(sorted_stack.pop())

    return unsorted_stack


unsorted_stack = Stack()
unsorted_stack.push(2)
unsorted_stack.push(4)
unsorted_stack.push(3)
unsorted_stack.push(1)
unsorted_stack.push(5)
print(sort_stack(unsorted_stack))

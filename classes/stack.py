class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def __repr__(self):
        out = []
        for i in range(len(self.stack)):
            out.append(str(self.stack[i]))
        return " -> ".join(out)

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if len(self.stack) < 1:
            return None
        self.size -= 1
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    # def size(self):
    #     return len(self.stack)

    # top of the stack
    def peek(self):
        if self.is_empty():
            return
        return self.stack[-1]


# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# print("Stack: ", my_stack)

# print(my_stack.size)
# # print("Removed item: ", my_stack.pop())
# # print("Stack", my_stack)
# print("Peek: ", my_stack.peek())

from classes.stack import Stack


class StackWithMin:
    def __init__(self):
        self.min_stack = Stack()
        self.stack = Stack()

    def __repr__(self):
        # out = f"{self.stack}\nmin_stack: {self.min_stack}"
        # out = "\n".join([str(self.stack), f"min_stack: {self.min_stack}"])

        # out = str(self.stack)
        # out += f"\nmin_stack{self.min_stack}"

        # out = ("stack: {}"
        #        "\n"
        #        "min_stack: {}").format(self.stack, self.min_stack)

        out = ("stack: {stack}"
               "\n"
               "min_stack: {min_stack}").format(stack=self.stack,
                                                min_stack=self.min_stack)

        # out = self.stack.__repr__() + "\n" + "min_stack: " + self.min_stack.__repr__()
        return out

    def push(self, item):
        if self.stack.is_empty():
            self.min_stack.push(item)
            self.stack.push(item)
        else:
            y = self.min_stack.peek()
            self.stack.push(item)
            if item < y:
                self.min_stack.push(item)
            else:
                self.min_stack.push(y)

    def pop(self):
        if self.stack.is_empty():
            return
        self.min_stack.pop()
        return self.stack.pop()

    def minimum(self):
        return self.min_stack.peek()


some_stack = StackWithMin()
some_stack.push(3)
some_stack.push(2)
some_stack.push(1)
some_stack.push(4)
print(some_stack)
# print(some_stack.min_stack)
print("Minimum: ", some_stack.minimum())
# print(some_stack.pop())
# print(some_stack.min_stack)

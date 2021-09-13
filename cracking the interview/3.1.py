class SpecialStack:
    NUMBER_OF_STACKS = 3

    def __init__(self, stack_size):
        self.stack_capacity = stack_size
        self.values = [0] * stack_size * self.NUMBER_OF_STACKS
        self.sizes = [0] * self.NUMBER_OF_STACKS

    def __repr__(self):
        return str(self.values)

    def push(self, stack_number, value):
        if self.is_full(stack_number):
            print("Full Stack")
            return
        self.sizes[stack_number] += 1
        self.values[self.index_of_top(stack_number)] = value

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            print("Stack is empty")
            return
        top_index = self.index_of_top(stack_number)
        top_value = self.values[top_index]
        self.values[top_index] = 0
        self.sizes[stack_number] -= 1
        return top_value

    #return top element
    def peek(self, stack_number):
        if self.is_empty(stack_number):
            print("Stack is empty")
            return
        return self.values[self.index_of_top(stack_number)]

    def is_full(self, stack_number):
        return self.sizes[stack_number] == self.stack_capacity

    def is_empty(self, stack_number):
        return self.sizes[stack_number] == 0

    def index_of_top(self, stack_number):
        offset = stack_number * self.stack_capacity
        size = self.sizes[stack_number]
        return offset + size - 1


stack = SpecialStack(3)
stack.push(0, 2)
stack.push(0, 1)
stack.push(1, 2)
stack.push(2, 2)
# print(stack)
# stack.pop(0)
print(stack)
print(stack.peek(0))

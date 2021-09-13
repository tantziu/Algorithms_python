from classes.stack import Stack


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.set_of_stacks = []

    def __repr__(self):
        out = []
        for i in range(len(self.set_of_stacks)):
            out.append(str(self.set_of_stacks[i]).__repr__())
        return "|".join(out)

    def get_last_stack(self):
        if not self.set_of_stacks:
            return None
        return self.set_of_stacks[-1]

    def push(self, item):
        last_stack = self.get_last_stack()
        if not self.set_of_stacks or last_stack.size == self.capacity:
            stack = Stack()
            stack.push(item)
            self.set_of_stacks.append(stack)
        else:
            last_stack.push(item)

    def pop(self):
        last_stack = self.get_last_stack()

        if not last_stack:
            return
        pop_item = last_stack.pop()
        if last_stack.size == 0:
            del self.set_of_stacks[-1]
        return pop_item

    def pop_at(self, index):
        # stack = self.set_of_stacks[index]
        stacks = len(self.set_of_stacks)
        if index > stacks - 1:
            return
        pop_item = self.set_of_stacks[index].pop()
        remaining = Stack()
        
        # if self.set_of_stacks[index].size == 0:
        #     del self.set_of_stacks[index]
        return pop_item


plates = SetOfStacks(2)
plates.push(1)
plates.push(2)
plates.push(3)
plates.push(4)
plates.push(5)
plates.push(6)
print(plates)
# plates.pop()
# plates.pop()
# plates.pop()
# print(plates)
plates.pop_at(1)
print(plates)



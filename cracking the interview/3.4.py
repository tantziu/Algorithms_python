from classes.stack import Stack


class MyQueue:
    def __init__(self):
        # self.my_queue = Stack()
        self.first_stack = Stack()
        self.second_stack = Stack()

    def __repr__(self):
        return

    #add
    def enqueue(self, item):
        self.first_stack.push(item)

    #remove
    def dequeue(self):
        if self.second_stack.size == 0:
            while self.first_stack.size != 0:
                item = self.first_stack.pop()
                self.second_stack.push(item)
        return self.second_stack.pop()

    #peek()
    # def peek(self):

    #is_empty()


my_queue = MyQueue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

print(my_queue.dequeue())
my_queue.enqueue(5)
print(my_queue.dequeue())
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.dequeue())

class Queue:
    def __init__(self):
        self.queue = []

    def __repr__(self):
        out = []
        for i in range(len(self.queue)):
            out.append(str(self.queue[i]))
        return "\n".join(out)

    #add
    def enqueue(self, item):
        return self.queue.append(item)

    #remove
    def dequeue(self):
        if self.is_empty():
            return
        item = self.queue[0]
        self.queue.pop(0)
        return item

    def peek(self):
        if self.is_empty():
            return
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

#
# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# my_queue.enqueue(4)
# my_queue.enqueue(5)
#
# my_queue.dequeue()
# my_queue.dequeue()
# print(my_queue)


from classes.queue import Queue
from datetime import datetime


class Animal:
    def __init__(self, name):
        self.name = name
        self.timestamp = None

    def __repr__(self):
        return self.name + str(self.timestamp)

    def add_timestamp(self, timestamp):
        self.timestamp = timestamp


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class Dog(Animal):
    pass


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        # self.counter = 0

    def enqueue(self, animal):
        # animal.add_timestamp(self.counter)
        # self.counter += 1
        animal.add_timestamp(datetime.now().timestamp())

        if isinstance(animal, Cat):
            self.cats.enqueue(animal)
        elif isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        return

    def dequeue_dog(self):
        return self.dogs.dequeue()

    def dequeue_cat(self):
        return self.cats.dequeue()

    def dequeue_any(self):
        cat_index = self.cats.peek().timestamp
        dog_index = self.dogs.peek().timestamp
        if cat_index < dog_index:
            return self.cats.dequeue()
        return self.dogs.dequeue()


animal_1 = Cat("Enzo")
# print(animal_1)
animal_2 = Dog("Bobic")
animal_3 = Cat("Sammy")
animal_4 = Cat("Snezka")
animal_queue = AnimalShelter()
animal_queue.enqueue(animal_1)
animal_queue.enqueue(animal_2)
animal_queue.enqueue(animal_3)
animal_queue.enqueue(animal_4)
# print(animal_queue.cats)
# print(animal_queue.dogs)
# print(animal_queue.dequeue_dog())
print(animal_queue.dequeue_cat())
print(animal_queue.dequeue_any())






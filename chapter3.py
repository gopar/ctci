from collections import deque

def prob3_2():
    """
    Design a stack which, in addition to push and pop, also has a function min
    which returns the minimum element? Push, Pop and min should operate in O(1)
    time.
    """
    class Stack:
        def __init__(self):
            self._stack = []
            self._min_list = []

        def push(self, data):
            try:
                if data <= self._min_list[-1]:
                    self._min_list.append(data)
            except IndexError:
                self._min_list = [data]
            finally:
                self._stack.append(data)

        def pop(self):
            data = self._stack.pop()
            if data == self._min_list[-1]:
                self._min_list.pop()
            return data

        @property
        def min(self):
            return self._min_list[-1]

    return Stack


def prob3_3():
    """
    Implement a data structure 'SetOfStacks' that will create a new stack once
    a height limit is reached. Push and Pop should still act the same as if it
    were a single stack.
    """
    class SetOfStacks:
        def __init__(self, height_limit=10):
            self.height_limit = height_limit
            self.set_of_stacks = [[]]

        def push(self, data):
            # If thresh hold is met, create a stack
            if len(self.set_of_stacks[-1]) >= self.height_limit:
                self.set_of_stacks.append([data])
            else:
                self.set_of_stacks[-1].append(data)

        def pop(self):
            if len(self.set_of_stacks[-1]) == 0:
                self.set_of_stacks.pop()
                return self.set_of_stacks[-1].pop()
            else:
                return self.set_of_stacks[-1].pop()

        def __len__(self):
            return len(self.set_of_stacks)

    return SetOfStacks


def prob3_5():
    """
    Implement a 'MyQueue' class which implements a queue using two stacks
    """
    class MyQueue:
        def __init__(self):
            self._stack_set = []
            self._queue_set = []

        def push(self, data):
            self._stack_set.append(data)

        def pop(self):
            self._turn_into_queue()
            return self._queue_set.pop()

        def _turn_into_queue(self):
            while len(self._stack_set) != 0:
                self._queue_set.append(self._stack_set.pop())

    return MyQueue


def prob3_6(stack):
    """
    Write a program to sort a stack in ascending order (biggest item on top)
    You may use additional stacks but you may not copy elements into any other
    data structure (such as an array).
    """
    ordered_stack = []

    while len(stack) != 0:
        tmp = stack.pop()
        while len(ordered_stack) != 0 and ordered_stack[-1] > tmp:
            stack.append(ordered_stack.pop())
        ordered_stack.append(tmp)

    return ordered_stack


def prob3_7():
    """
    An animal shelter holds only dogs and cats, and operates strictly
    'first in, first out' basis. People must adopt either the 'oldest'
    (based on arrival time) or they can select whether they would
    prefer a dog or cat (and receive the oldest of that type). They cannot
    select specific animal. Create the data structure to main this system
    and implement operations such as 'enqueue', 'dequeueAny', dequeueDog
    and dequeueCat. You can use LinkedList
    """
    class Dog:
        def __init__(self, name):
            self.name = name
            self.time = None

    class Cat:
        def __init__(self, name):
            self.name = name
            self.time = None

    class AnimalShelter:
        def __init__(self):
            self.count = 0
            self.dogs = deque()
            self.cats = deque()

        def enqueue(self, animal):
            animal.time = self.count

            if isinstance(animal, Dog):
                self.dogs.append(animal)
            else:
                self.cats.append(animal)

            self.count += 1

        def dequeAny(self):
            if len(self.dogs) == 0:
                return self.cats.pop()
            if len(self.cats) == 0:
                return self.dogs.pop()

            if self.dogs[-1].time > self.cats[-1].time:
                return self.dequeDog()
            return self.dequeCat()

        def dequeCat(self):
            return self.cats.pop()

        def dequeDog(self):
            return self.dogs.pop()

    return AnimalShelter, Cat, Dog

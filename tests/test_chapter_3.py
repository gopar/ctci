import unittest

import chapter3


class Chapter3(unittest.TestCase):

    def test_chapter3_2(self):
        stack = chapter3.prob3_2()()

        stack.push(3)
        stack.push(9)
        stack.push(1)

        self.assertEqual(stack.min, 1)
        stack.pop()
        self.assertEqual(stack.min, 3)
        stack.pop()
        self.assertEqual(stack.min, 3)

    def test_chapter3_3(self):
        setOfStacks = chapter3.prob3_3()()

        for x in range(21):
            setOfStacks.push(x)

        self.assertEqual(len(setOfStacks), 3)
        setOfStacks.pop()

        nineteen = setOfStacks.pop()
        self.assertEqual(nineteen, 19)

        setOfStacks.pop()
        self.assertEqual(len(setOfStacks), 2)

    def test_chapter3_5(self):
        myQueue = chapter3.prob3_5()()

        for x in range(10):
            myQueue.push(x)

        for index, x in enumerate(range(10)):
            self.assertEqual(myQueue.pop(), index)

    def test_chapter3_6(self):
        stack = [5, 4, 3]
        new_stack = chapter3.prob3_6(stack)

        stack = [3, 4, 5]
        while len(new_stack) != 0:
            self.assertEqual(stack.pop(), new_stack.pop())

    def test_chapter3_7(self):
        AnimalShelter, Cat, Dog = chapter3.prob3_7()

        shelter = AnimalShelter()

        for x in range(10):
            shelter.enqueue(Cat(str(x)))

        for x in range(10, 20):
            shelter.enqueue(Dog(str(x)))

        self.assertEqual(shelter.dequeCat().name, '9')
        self.assertEqual(shelter.dequeDog().name, '19')

        animal = shelter.dequeAny()
        self.assertIsInstance(animal, Dog)

        for x in range(8):
            self.assertIsInstance(shelter.dequeAny(), Dog)
        for x in range(9):
            self.assertIsInstance(shelter.dequeAny(), Cat)

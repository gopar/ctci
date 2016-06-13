import chapter3


def test_chapter3_2():
    stack = chapter3.prob3_2()()

    stack.push(3)
    stack.push(9)
    stack.push(1)

    assert stack.min == 1
    stack.pop()
    assert stack.min == 3
    stack.pop()
    assert stack.min, 3


def test_chapter3_3():
    setOfStacks = chapter3.prob3_3()()

    for x in range(21):
        setOfStacks.push(x)

    assert len(setOfStacks) == 3
    setOfStacks.pop()

    nineteen = setOfStacks.pop()
    assert nineteen == 19

    setOfStacks.pop()
    assert len(setOfStacks) == 2


# TODO: Parametrize
def test_chapter3_5():
    myQueue = chapter3.prob3_5()()

    for x in range(10):
        myQueue.push(x)

    for index, x in enumerate(range(10)):
        assert myQueue.pop() == index


# TODO: Parametrize
def test_chapter3_6():
    stack = [5, 4, 3]
    new_stack = chapter3.prob3_6(stack)

    stack = [3, 4, 5]
    while len(new_stack) != 0:
        assert stack.pop() == new_stack.pop()


# TODO: Parametrize
def test_chapter3_7():
    AnimalShelter, Cat, Dog = chapter3.prob3_7()

    shelter = AnimalShelter()

    for x in range(10):
        shelter.enqueue(Cat(str(x)))

    for x in range(10, 20):
        shelter.enqueue(Dog(str(x)))

    assert shelter.dequeCat().name == '9'
    assert shelter.dequeDog().name == '19'

    animal = shelter.dequeAny()
    assert animal, Dog

    for x in range(8):
        assert isinstance(shelter.dequeAny(), Dog)
    for x in range(9):
        assert isinstance(shelter.dequeAny(), Cat)

def prob9_1(steps, possible_ways=0, cache={}):
    """
    A child is running up a staircase with n steps, and can hop
    either 1, 2 or 3 steps at a time. Implement a method to count how many
    possible ways the child ca run up the stairs
    """
    if steps < 0:
        return 0
    if steps == 0:
        return 1

    if cache.get(steps, None):
        return cache[steps]

    possible_ways += prob9_1(steps - 1)
    possible_ways += prob9_1(steps - 2)
    possible_ways += prob9_1(steps - 3)

    cache[steps] = possible_ways

    return cache[steps]


if __name__ == '__main__':
    print(prob9_1(3))
    print(prob9_1(4))

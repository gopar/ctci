from collections import Counter


def prob1_1(string):
    """
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    """
    # I'm going to assume string is in ASCII
    if len(string) > 256:
        return False

    # The highest value should be 1, cause each letter should only appear once
    return max([v for k, v in Counter(string).items()]) == 1

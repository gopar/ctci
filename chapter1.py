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


def prob1_2(string):
    """
    Implement a function void reverse(char* str) in C/C++ which reverses a
    null-terminated string.

    Well this is Python, so I'm doing it in Python \o/
    """
    return string[::-1]


def prob1_3(s1, s2):
    """
    Given two strings, write a method to decide if one is a permutation
    of the other.
    """
    return sorted(s1) == sorted(s2)


def prob1_4(string):
    """
    Write a method to replace all spaces in a string with '%20'. You may assume
    that the string ha sufficient space at the end of the string to hold the
    additional characters and you are given the true length of the string

    Ex:
    input: 'Mr John Smith    '
    output:'Mr%20John$20Smith'
    """
    return string.replace(' ', '%20')


def prob1_5(string):
    """
    Implement a method to perform basic string compression using the counts of
    repeated characters. For example, 'aabccccaa' would become 'a2b1c4a2'.
    If the 'compressed' string would not become smaller than the original string
    your method should return the original string.
    """
    new_string = ''.join([k + str(v) for k, v in Counter(string).items()])

    return new_string if len(new_string) < len(string) else string


def prob1_6(matrix, n):
    """
    Given an image represented by MxN matrix, where each pixel in the image is
    4 bytes, wite a method to rotate the image by 90 degrees.
    Can you do this in place?
    """
    # Book answer :(
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # Save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return matrix


def prob1_7(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its
    entire row and column are set to 0
    """
    rows = []
    cols = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                rows.append(row)
                cols.append(col)

    # Update rows and colums
    for row in range(len(matrix)):
        if row in rows:
            matrix[row] = [0] * len(matrix[0])
        for col in cols:
            matrix[row][col] = 0

    return matrix


def prob1_8(s1, s2):
    """
    Assume you have a method isSubstring which checks if one word is a
    sub-string of another. Given two strings, s1 and s2, write code to check if
    s2 is a rotation of s1 using only one call to isSubstring

    Ex:
    'waterbottle' is a rotation of 'erbottlewat'
    """

    return s2 in (s1 + s1)

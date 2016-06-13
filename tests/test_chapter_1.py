import chapter1


def test_chapter1_1():
    s = '12345'
    assert chapter1.prob1_1(s) is True
    assert chapter1.prob1_1(s + '1') is False


def test_chapter1_2():
    s = '12345'
    assert '54321' == chapter1.prob1_2(s)
    assert s != chapter1.prob1_2(s)


def test_chapter1_3():
    s1 = '54321'
    s2 = '12345'
    assert chapter1.prob1_3(s1, s2) is True
    assert chapter1.prob1_3(s1, s1) is True
    assert chapter1.prob1_3(s2, s2) is True
    assert chapter1.prob1_3(s1, s2 + '1') is False


def test_chapter1_4():
    s = 're ra ro'
    assert 're%20ra%20ro' == chapter1.prob1_4(s)
    assert 're ra ro' != chapter1.prob1_4(s)


def test_chapter1_5():
    s = 'aaa'
    assert 'a3' == chapter1.prob1_5(s)
    assert 'a2' != chapter1.prob1_5('aa')
    assert 'a' == chapter1.prob1_5('a')


def test_chapter1_6():
    matrix = [[1, 2],
              [3, 4]]
    output = [[3, 1],
              [4, 2]]

    assert output == chapter1.prob1_6(matrix, 2)


def test_chapter1_7():
    matrix = [[0, 1],
              [1, 0]]
    output = [[0, 0],
              [0, 0]]

    assert output == chapter1.prob1_7(matrix)


def test_chapter1_8():
    s1 = 'hello'
    s2 = 'llohe'

    assert chapter1.prob1_8(s1, s2) is True

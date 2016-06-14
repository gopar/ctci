import pytest

import chapter1

ONE_THROUGH_FIVE = '12345'


@pytest.mark.parametrize('s,expected', [
    (ONE_THROUGH_FIVE, True),
    (ONE_THROUGH_FIVE + '1', False),
    ('0' * 300, False),
])
def test_chapter1_1(s, expected):
    assert chapter1.prob1_1(s) is expected


@pytest.mark.parametrize('s,expected', [
    (ONE_THROUGH_FIVE, ONE_THROUGH_FIVE[::-1]),
    ('1', '1'),
])
def test_chapter1_2(s, expected):
    assert chapter1.prob1_2(s) == expected


@pytest.mark.parametrize('s1,s2', [
    (ONE_THROUGH_FIVE, ONE_THROUGH_FIVE[::-1]),
])
def test_chapter1_3(s1, s2):
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


@pytest.mark.parametrize('matrix,expected', [
    ([[0, 1],
      [1, 0]], [[0, 0],
                [0, 0]]),
    ([[0, 1, 1],
      [1, 0, 1]], [[0, 0, 0],
                   [0, 0, 0]])
])
def test_chapter1_7(matrix, expected):
    assert expected == chapter1.prob1_7(matrix)


def test_chapter1_8():
    s1 = 'hello'
    s2 = 'llohe'

    assert chapter1.prob1_8(s1, s2) is True

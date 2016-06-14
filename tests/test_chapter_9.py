import pytest


import chapter9


@pytest.mark.parametrize('step, expect', [
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 7),
])
def test_chapter9_1(step, expect):
    result = chapter9.prob9_1(step)
    assert result == expect


@pytest.mark.parametrize('array, expect', [
    ([0, 1, 2, 3], True),
    ([0], True),
    ([0.1], False),
    ([], True),
    ([90], False)
])
def test_chapter9_3(array, expect):
    assert chapter9.prob9_3(array) is expect

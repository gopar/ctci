import chapter2
from utils import ListNode


def test_chapter2_1():
    node = ListNode(1, ListNode(2, ListNode(1, ListNode(4))))
    node = chapter2.prob2_1(node)
    _sum = 0

    while node is not None:
        _sum += node.data
        node = node.next

    assert 7 == _sum


def test_chapter2_2():
    node = ListNode(1, ListNode(2, ListNode(1, ListNode(4))))
    assert 4 == chapter2.prob2_2(node, 1).data

    node = ListNode(90)
    assert 90 == chapter2.prob2_2(node, 1).data


def test_chapter2_3():
    node = ListNode('a', ListNode('b', ListNode(
        'c', ListNode('d', ListNode('e')))))
    node_to_be_delete = node.next.next

    chapter2.prob2_3(node_to_be_delete)

    while node is not None:
        assert 'c' != node.data
        node = node.next

    assert chapter2.prob2_3(None) is None


def test_chapter2_4():
    node = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    output = [1, 2, 3, 4, 5]

    node = chapter2.prob2_4(node, 0)
    answer = []

    while node is not None:
        answer.append(node.data)
        node = node.next

    assert output == answer
    assert chapter2.prob2_4(None, 0) is None


def test_chapter2_5():
    left = ListNode(7, ListNode(1, ListNode(6)))
    right = ListNode(5, ListNode(9, ListNode(2)))

    output = ListNode(2, ListNode(1, ListNode(9)))

    node = chapter2.prob2_5(left, right)

    while node is not None:
        assert node.data == output.data
        node = node.next
        output = output.next

    assert chapter2.prob2_5(None, None) is None

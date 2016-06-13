import pytest

import chapter4
from utils import TreeNode

FIVE_ONE_TEN = (5, 1, 10)
FIVE_ZERO_TWENTY = (5, 0, 20)


def test_chapter4_1():
    root = TreeNode(0, TreeNode(1), TreeNode(2))

    assert chapter4.prob4_1(root) is True

    uneven = TreeNode(3, TreeNode(8, TreeNode(9)))
    assert chapter4.prob4_1(uneven) is False


def test_chapter4_2():
    graph = {
        'A': ['C', 'B'],
        'B': ['D'],
    }
    assert chapter4.prob4_2()(graph, 'A', 'D') == ['A', 'B', 'D']
    assert chapter4.prob4_2()(graph, 'B', 'C') is None


def test_chapter4_3():
    _list = [1, 2, 3, 4, 5, 6, 7]
    root = chapter4.prob4_3()(_list, 0, len(_list) - 1)

    assert root.data == 4
    assert root.left.data == 2
    assert root.right.data == 6

    # Is tree balanced?
    assert chapter4.prob4_1(root) is True


# TODO: Parametrize
def test_chapter4_4():
    tree = TreeNode('A', TreeNode('B'), TreeNode('C'))

    result = chapter4.prob4_4()(tree)
    _list = ['A', 'B', 'C']

    i = 0
    for node in result:
        root = node
        while root is not None:
            assert root.data == _list[i]
            root = root.next
            i += 1

    assert len(result) == 2


@pytest.mark.parametrize("root,left,right", [
    FIVE_ONE_TEN,
    FIVE_ZERO_TWENTY,
])
def test_chapter4_5(root, left, right):
    tree = TreeNode(root, TreeNode(left), TreeNode(right))
    result = chapter4.prob4_5(tree)

    assert result is True

    tree = TreeNode(root, TreeNode(right), TreeNode(left))
    result = chapter4.prob4_5(tree)

    assert result is False


@pytest.mark.parametrize("root,left,right,parent", [
    FIVE_ONE_TEN + (100, ),
    FIVE_ZERO_TWENTY + (200, ),
])
def test_chapter4_8(root, left, right, parent):
    tree = TreeNode(root, TreeNode(left), TreeNode(right))
    root = TreeNode(parent)
    root.left = tree

    assert chapter4.prob4_8(root, tree) is True

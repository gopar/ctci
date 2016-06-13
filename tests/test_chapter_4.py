import chapter4


def test_chapter4_1():
    Node = chapter4.Node
    root = Node(0, Node(1), Node(2))

    assert chapter4.prob4_1(root) is True

    uneven = Node(3, Node(8, Node(9)))
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
    Node = chapter4.Node
    tree = Node('A', Node('B'), Node('C'))

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

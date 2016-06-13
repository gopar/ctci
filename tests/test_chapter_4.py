import unittest

import chapter4


class Chapter4(unittest.TestCase):
    def test_chapter4_1(self):
        Node = chapter4.Node
        root = Node(0, Node(1), Node(2))
        self.assertEqual(chapter4.prob4_1(root), True)

        uneven = Node(3, Node(8, Node(9)))
        self.assertEqual(chapter4.prob4_1(uneven), False)

    def test_chapter4_2(self):
        graph = {
            'A': ['C', 'B'],
            'B': ['D'],
        }
        self.assertEqual(chapter4.prob4_2()(graph, 'A', 'D'), ['A', 'B', 'D'])
        self.assertEqual(chapter4.prob4_2()(graph, 'B', 'C'), None)

    def test_chapter4_3(self):
        _list = [1, 2, 3, 4, 5, 6, 7]
        root = chapter4.prob4_3()(_list, 0, len(_list) - 1)

        self.assertEqual(root.data, 4)
        self.assertEqual(root.left.data, 2)
        self.assertEqual(root.right.data, 6)

        # Is tree balanced?
        self.assertTrue(chapter4.prob4_1(root))

    def test_chapter4_4(self):
        Node = chapter4.Node
        tree = Node('A', Node('B'), Node('C'))

        result = chapter4.prob4_4()(tree)
        _list = ['A', 'B', 'C']

        i = 0
        for node in result:
            root = node
            while root is not None:
                self.assertEqual(root.data, _list[i])
                root = root.next
                i += 1

        self.assertEqual(len(result), 2)

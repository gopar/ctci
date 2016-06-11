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

import unittest

import chapter2
from chapter2 import Node


class Chapter2(unittest.TestCase):
    def test_chapter2_1(self):
        node = Node(1, Node(2, Node(1, Node(4))))
        node = chapter2.prob2_1(node)
        _sum = 0

        while node is not None:
            _sum += node.data
            node = node.next

        self.assertEqual(7, _sum)

    def test_chapter2_2(self):
        node = Node(1, Node(2, Node(1, Node(4))))
        self.assertEqual(4, chapter2.prob2_2(node, 1).data)

        node = Node(90)
        self.assertEqual(90, chapter2.prob2_2(node, 1).data)

    def test_chapter2_3(self):
        node = Node('a', Node('b', Node('c', Node('d', Node('e')))))
        node_to_be_delete = node.next.next

        chapter2.prob2_3(node_to_be_delete)

        while node is not None:
            self.assertNotEqual('c', node.data)
            node = node.next

    def test_chapter2_4(self):
        node = Node(5, Node(4, Node(3, Node(2, Node(1)))))
        output = [1, 2, 3, 4, 5]

        node = chapter2.prob2_4(node, 0)
        answer = []

        while node is not None:
            answer.append(node.data)
            node = node.next

        self.assertEqual(output, answer)

    def test_chapter2_5(self):
        left = Node(7, Node(1, Node(6)))
        right = Node(5, Node(9, Node(2)))

        output = Node(2, Node(1, Node(9)))

        node = chapter2.prob2_5(left, right)

        while node is not None:
            self.assertEqual(node.data, output.data)
            node = node.next
            output = output.next

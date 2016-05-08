import unittest

import chapter1


class Chapter1(unittest.TestCase):
    def test_chapter1_1(self):
        s = '12345'
        self.assertTrue(chapter1.prob1_1(s))
        self.assertFalse(chapter1.prob1_1(s + '1'))

    def test_chapter1_2(self):
        s = '12345'
        self.assertEqual('54321', chapter1.prob1_2(s))
        self.assertNotEqual(s, chapter1.prob1_2(s))

    def test_chapter1_3(self):
        s1 = '54321'
        s2 = '12345'
        self.assertTrue(chapter1.prob1_3(s1, s2))
        self.assertTrue(chapter1.prob1_3(s1, s1))
        self.assertTrue(chapter1.prob1_3(s2, s2))
        self.assertFalse(chapter1.prob1_3(s1, s2 + '1'))

    def test_chapter1_4(self):
        s = 're ra ro'
        self.assertEqual('re%20ra%20ro', chapter1.prob1_4(s))
        self.assertNotEqual('re ra ro', chapter1.prob1_4(s))

    def test_chapter1_5(self):
        s = 'aaa'
        self.assertEqual('a3', chapter1.prob1_5(s))
        self.assertNotEqual('a2', chapter1.prob1_5('aa'))
        self.assertEqual('a', chapter1.prob1_5('a'))

    def test_chapter1_6(self):
        matrix = [[1, 2],
                  [3, 4]]
        output = [[3, 1],
                  [4, 2]]

        self.assertEqual(output, chapter1.prob1_6(matrix, 2))

    def test_chapter1_7(self):
        matrix = [[0, 1],
                  [1, 0]]
        output = [[0, 0],
                  [0, 0]]

        self.assertEqual(output, chapter1.prob1_7(matrix))

    def test_chapter1_8(self):
        s1 = 'hello'
        s2 = 'llohe'

        self.assertTrue(chapter1.prob1_8(s1, s2))

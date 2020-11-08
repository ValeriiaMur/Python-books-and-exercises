import unittest
from searching import *


class SearchingTests(unittest.TestCase):
    def test_linear_search(self):
        arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
        arr2 = []

        self.assertEqual(linear_search(arr1, 6), -1)
        self.assertEqual(linear_search(arr1, -6), 8)
        self.assertEqual(linear_search(arr1, 0), 6)
        self.assertEqual(linear_search(arr2, 3), -1)

    def test_binary_search(self):
        arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
        arr2 = []

        self.assertEqual(binary_search(arr1, -8), 1)
        self.assertEqual(binary_search(arr1, 0), 6)
        self.assertEqual(binary_search(arr2, 6), -1)
        self.assertEqual(binary_search(arr2, 0), -1)


if __name__ == '__main__':
    unittest.main()

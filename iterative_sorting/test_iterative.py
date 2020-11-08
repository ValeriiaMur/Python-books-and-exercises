import unittest
import random
from iterative_sorting import *

class IterativeSortingTest(unittest.TestCase):
    def test_selection_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [0, 1, 2, 3, 4, 5]
        arr4 = random.sample(range(200), 50)

        self.assertEqual(selection_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(selection_sort(arr2), [])
        self.assertEqual(selection_sort(arr3), [0,1,2,3,4,5])
        self.assertEqual(selection_sort(arr4), sorted(arr4))

    def test_bubble_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [0, 1, 2, 3, 4, 5]
        arr4 = random.sample(range(200), 50)

        self.assertEqual(bubble_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(bubble_sort(arr2), [])
        self.assertEqual(bubble_sort(arr3), [0,1,2,3,4,5])
        self.assertEqual(bubble_sort(arr4), sorted(arr4))

    # Uncomment this test to test your count_sort implementation
    # def test_counting_sort(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [1, 5, -2, 4, 3]
    #     arr4 = random.sample(range(200), 50)

    #     self.assertEqual(counting_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(counting_sort(arr2), [])
    #     self.assertEqual(counting_sort(arr3), "Error, negative numbers not allowed in Count Sort")
    #     self.assertEqual(counting_sort(arr4), sorted(arr4))


if __name__ == '__main__':
    unittest.main()

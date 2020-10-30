import unittest
from unittest.mock import MagicMock
from generic_heap import Heap

class HeapTests(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()

    def test_default_heap_insert_works(self):
        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5) 
        self.assertEqual(self.heap.storage, [10, 9, 9, 6, 1, 8, 9, 5])

    def test_default_get_priority_works(self):
        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        self.assertEqual(self.heap.get_size(), 8)
        self.assertEqual(self.heap.get_priority(), 10)

    def test_default_get_priority_after_delete(self):
        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 9)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 9)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 9)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 8)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 6)

    def test_default_delete_elements_in_order(self):
        self.heap.insert(6)
        self.heap.insert(7)
        self.heap.insert(5)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(5)

        descending_order = []

        while self.heap.get_size() > 0:
            descending_order.append(self.heap.delete())

        self.assertEqual(descending_order, [10, 8, 7, 6, 5, 5, 2, 1])

    def test_custom_heap_insert_works(self):
        self.heap = Heap(lambda x, y: x < y)

        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5) 
        self.assertEqual(self.heap.storage, [1, 5, 9, 6, 8, 10, 9, 9])

    def test_custom_get_priority_works(self):
        self.heap = Heap(lambda x, y: x < y)

        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        self.assertEqual(self.heap.get_size(), 8)
        self.assertEqual(self.heap.get_priority(), 1)

    def test_custom_get_priority_after_delete(self):
        self.heap = Heap(lambda x, y: x < y)

        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 5)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 6)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 8)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 9)
        self.heap.delete()
        self.assertEqual(self.heap.get_priority(), 9)

    def test_custom_delete_elements_in_order(self):
        self.heap = Heap(lambda x, y: x < y)

        self.heap.insert(6)
        self.heap.insert(7)
        self.heap.insert(5)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(5)

        ascending_order = []

        while self.heap.get_size() > 0:
            ascending_order.append(self.heap.delete())

        self.assertEqual(ascending_order, [1, 2, 5, 5, 6, 7, 8, 10])

    def test_bubble_up_was_called(self):
        self.heap._bubble_up = MagicMock()
        self.heap.insert(5)
        self.assertTrue(self.heap._bubble_up.called)

    def test_sift_down_was_called(self):
        self.heap._sift_down = MagicMock()
        self.heap.insert(10)
        self.heap.insert(11)
        self.heap.delete()
        self.assertTrue(self.heap._sift_down.called)


if __name__ == '__main__':
    unittest.main()

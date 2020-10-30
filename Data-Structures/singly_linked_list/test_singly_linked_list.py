import unittest
from singly_linked_list import LinkedList

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_add_to_tail(self):
        self.list.add_to_tail(1)
        self.assertEqual(self.list.tail.value, 1)
        self.assertEqual(self.list.head.value, 1)
        self.list.add_to_tail(2)
        self.assertEqual(self.list.tail.value, 2)
        self.assertEqual(self.list.head.value, 1)

    def test_remove_head(self):
        self.list.add_to_tail(10)
        self.list.add_to_tail(20)
        self.assertEqual(self.list.remove_head(), 10)
        self.assertEqual(self.list.remove_head(), 20)

        self.list.add_to_tail(10)    
        self.assertEqual(self.list.remove_head(), 10)    
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertIsNone(self.list.remove_head())

    def test_remove_tail(self):
        self.list.add_to_tail(30)
        self.list.add_to_tail(40)
        self.assertEqual(self.list.remove_tail(), 40)
        self.assertEqual(self.list.remove_tail(), 30)

        self.list.add_to_tail(100)    
        self.assertEqual(self.list.remove_tail(), 100)    
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertIsNone(self.list.remove_tail())

if __name__ == '__main__':
    unittest.main()

import unittest
from reverse import LinkedList

class LinkedListTests(unittest.TestCase):
  def setUp(self):
    self.list = LinkedList()

  def test_add_to_head(self):
    self.list.add_to_head(1)
    self.assertEqual(self.list.head.value, 1)
    self.list.add_to_head(2)
    self.assertEqual(self.list.head.value, 2)

  def test_contains(self):
    self.list.add_to_head(1)
    self.list.add_to_head(2)
    self.list.add_to_head(10)
    self.assertTrue(self.list.contains(2))
    self.assertTrue(self.list.contains(10))
    self.assertFalse(self.list.contains(1000))

  def test_empty_reverse(self):
    self.list.reverse_list(self.list.head, None)
    self.assertEqual(self.list.head, None)
    
  def test_single_reverse(self):
    self.list.add_to_head(1)
    self.list.reverse_list(self.list.head, None)
    self.assertEqual(self.list.head.value, 1)

  def test_longer_reverse(self):
    self.list.add_to_head(1)
    self.list.add_to_head(2)
    self.list.add_to_head(3)
    self.list.add_to_head(4)
    self.list.add_to_head(5)
    self.assertEqual(self.list.head.value, 5)
    self.list.reverse_list(self.list.head, None)
    self.assertEqual(self.list.head.value, 1)
    self.assertEqual(self.list.head.get_next().value, 2)
    self.assertEqual(self.list.head.get_next().get_next().value, 3)
    
if __name__ == '__main__':
  unittest.main()
import unittest
from stack import Stack

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_len_returns_0_for_empty_stack(self):
        self.assertEqual(len(self.stack), 0)

    def test_len_returns_correct_length_after_push(self):
        self.assertEqual(len(self.stack), 0)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 1)
        self.stack.push(4)
        self.assertEqual(len(self.stack), 2)
        self.stack.push(6)
        self.stack.push(8)
        self.stack.push(10)
        self.stack.push(12)
        self.stack.push(14)
        self.stack.push(16)
        self.stack.push(18)
        self.assertEqual(len(self.stack), 9)

    def test_empty_pop(self):
        self.assertIsNone(self.stack.pop())
        self.assertEqual(len(self.stack), 0)

    def test_pop_respects_order(self):
        self.stack.push(100)
        self.stack.push(101)
        self.stack.push(105)
        self.assertEqual(self.stack.pop(), 105)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 101)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.pop(), 100)
        self.assertEqual(len(self.stack), 0)
        self.assertIsNone(self.stack.pop())
        self.assertEqual(len(self.stack), 0)


if __name__ == '__main__':
    unittest.main()

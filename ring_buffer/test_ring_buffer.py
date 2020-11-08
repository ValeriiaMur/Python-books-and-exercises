import unittest
from ring_buffer import RingBuffer

class RingBufferTests(unittest.TestCase):
    def setUp(self):
        self.capacity = 5
        self.buffer = RingBuffer(self.capacity)
    
    def test_new_buffer_has_appropriate_capacity(self):
        self.assertEqual(self.buffer.capacity, self.capacity)

    def test_adding_one_element_to_buffer(self):
        self.buffer.append('a')
        self.assertEqual(self.buffer.get(), ['a'])

    def test_filling_buffer_to_capacity(self):
        self.buffer.append('a')
        self.buffer.append('b')
        self.buffer.append('c')
        self.buffer.append('d')
        self.buffer.append('e')
        self.assertEqual(self.buffer.get(), ['a', 'b', 'c', 'd', 'e'])

    def test_adding_one_element_to_full_buffer(self):
        self.buffer.append('a')
        self.buffer.append('b')
        self.buffer.append('c')
        self.buffer.append('d')
        self.buffer.append('e')
        self.buffer.append('f')
        self.assertEqual(self.buffer.get(), ['f', 'b', 'c', 'd', 'e'])

    def test_adding_many_elements_to_full_buffer(self):
        self.buffer.append('a')
        self.buffer.append('b')
        self.buffer.append('c')
        self.buffer.append('d')
        self.buffer.append('e')
        self.buffer.append('f')
        self.buffer.append('g')
        self.buffer.append('h')
        self.buffer.append('i')
        self.assertEqual(self.buffer.get(), ['f', 'g', 'h', 'i', 'e'])

    def test_adding_50_elements_to_buffer(self):
        for i in range(50):
            self.buffer.append(i)

        self.assertEqual(self.buffer.get(), [45, 46, 47, 48, 49])

if __name__ == '__main__':
    unittest.main()
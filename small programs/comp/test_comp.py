import unittest
from comp import *

def compare_humans(inp, exp):
  if len(inp) != len(exp):
    return False
  for i in range(len(inp)):
    if inp[i].name != exp[i].name:
      return False
    if inp[i].age != exp[i].age:
      return False
  return True

class CompTests(unittest.TestCase):
  def test_starts_with_D(self):
    self.assertEqual(a, ['Daphne', 'David'])

  def test_ends_with_e(self):
    self.assertEqual(b, ['Alice', 'Charlie', 'Daphne', 'Eve'])

  def test_between_C_and_G(self):
    self.assertEqual(c, ['Charlie', 'Daphne', 'Eve', 'Frank', 'Glenn', 'David'])

  def test_ages_plus_10(self):
    self.assertEqual(d, [39, 42, 47, 40, 36, 28, 52, 22, 51, 41])

  def test_name_hyphen_age(self):
    self.assertEqual(e, ['Alice-29', 'Bob-32', 'Charlie-37', 'Daphne-30', 'Eve-26', 'Frank-18', 'Glenn-42', 'Harrison-12', 'Igon-41', 'David-31'])

  def test_names_ages_between_27_and_32(self):
    self.assertEqual(f, [('Alice', 29), ('Bob', 32), ('Daphne', 30), ('David', 31)])

  def test_all_names_uppercase(self):
    expected = [Human("ALICE", 34), Human("BOB", 37), Human("CHARLIE", 42), Human("DAPHNE", 35), Human("EVE", 31), Human("FRANK", 23), Human("GLENN", 47), Human("HARRISON", 17), Human("IGON", 46), Human("DAVID", 36)]
    self.assertTrue(compare_humans(g, expected))

  def test_square_root_of_ages(self):
    self.assertEqual(h, [5.385164807134504, 5.656854249492381, 6.082762530298219, 5.477225575051661, 5.0990195135927845, 4.242640687119285, 6.48074069840786, 3.4641016151377544, 6.4031242374328485, 5.5677643628300215])


if __name__ == '__main__':
  unittest.main()

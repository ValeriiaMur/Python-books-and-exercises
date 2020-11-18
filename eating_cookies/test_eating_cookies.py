import unittest
from eating_cookies import eating_cookies

class Test(unittest.TestCase):

  def test_eating_cookies_small_n(self):
    self.assertEqual(eating_cookies(0), 1)
    self.assertEqual(eating_cookies(1), 1)
    self.assertEqual(eating_cookies(2), 2)
    self.assertEqual(eating_cookies(5), 13)
    self.assertEqual(eating_cookies(10), 274)

  def test_eating_cookies_large_n(self):
    self.assertEqual(eating_cookies(50, [0 for i in range(51)]), 10562230626642)
    self.assertEqual(eating_cookies(100, [0 for i in range(101)]), 180396380815100901214157639)
    self.assertEqual(eating_cookies(500, [0 for i in range(501)]), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)


if __name__ == '__main__':
  unittest.main()
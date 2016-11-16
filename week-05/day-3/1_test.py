from exercise1 import divide_ten
import unittest
class TestMyFunctions(unittest.TestCase):

    def test_divide_ten_with_two(self):
        self.assertEqual(divide_ten(2), 5)
        self.assertEqual(divide_ten(0), 'fail')

if __name__ == '__main__':
    unittest.main(exit=False)

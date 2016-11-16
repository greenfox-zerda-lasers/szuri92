from exercise2 import line_number
import unittest
class TestMyFunctions(unittest.TestCase):

    def test_my_function_line_number(self):
        self.assertEqual(line_number('test_text.txt'), 6)
        self.assertEqual(line_number('test_texts.txt'), 0)
        self.assertEqual(line_number(12), 'Give a valid file name!')

if __name__ == '__main__':
    unittest.main(exit=False)

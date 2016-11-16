from exercise3 import Person
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_valami(self):
        self.assertRaises(ValueError, Person, 'kovacs', 'Bela', 2112)







if __name__ == '__main__':
    unittest.main(exit=False)

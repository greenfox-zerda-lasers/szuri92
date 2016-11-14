from szurovecz_mate_work import anagramm, count_letters
import unittest
#from collections import Counter

class TestMyFunctions(unittest.TestCase):
    def test_if_simple_strings_true(self):
        self.assertTrue(anagramm('lajos', 'solja'), True)
    def test_if_lower_and_upper_equal(self):
        self.assertTrue(anagramm('lajos', 'SoJla'))
    def test_if_normal_and_spaced_is_true(self):
        self.assertFalse(anagramm('lajos', 'Llojas'))
    def test_if_int_false(self):
        self.assertRaises(AttributeError, anagramm, 'lajos', 15)


    def test_if_count_upper_letter(self):
        self.assertEqual(count_letters('BElLLLaaA'), ({'b' : 1, 'e': 1, 'l' : 4, 'a': 3}))
    def test_count_letter_easy_string(self):
        self.assertEqual(count_letters('Jozsi'), {'j' : 1, 'o': 1, 'z' : 1, 's': 1, 'i' : 1})
    def test_count_letter_empty_string(self):
        self.assertEqual(count_letters(''), {})
    def test_count_for_non_letter(self):
        self.assertEqual(count_letters('be12@la!'), {'b': 1, 'a': 1, 'e' : 1, 'l': 1})
    def test_count_for_weird_ascii(self):
        self.assertEqual(count_letters('ßåélee'), {'ß': 1, 'å': 1, 'é': 1, 'l': 1, 'e': 2})
    def test_count_for_int(self):
        self.assertRaises(AttributeError, count_letters, 12)
    def test_count_for_list(self):
        self.assertRaises(AttributeError, count_letters, [1, 1, 2, 3, 5, 7, 'a', 'v'])
    def test_count_for_list(self):
        self.assertRaises(AttributeError, count_letters, ['a', 'v', 'c'])



if __name__ == '__main__':
    unittest.main(exit=False)

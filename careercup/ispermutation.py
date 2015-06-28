"""
Given two strings, write a method to decide if one is a permutation of the other
"""
import unittest

def is_permutation(a,b):
    if len(a) != len(b):
        return False
    if sorted(a) == sorted(b):
        return True
    return False

class TestPerm(unittest.TestCase):
    def test_different_len(self):
        self.assertEqual(is_permutation("senthil","etinhl"),False)
    def test_repeats(self):
        self.assertEqual(is_permutation("aaa","aaa"),True)
    def test_reverse(self):
        self.assertEqual(is_permutation("senthil","lihtnes"),True)

if __name__ == "__main__":
    unittest.main()

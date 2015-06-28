"""
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
"""

import unittest

def isunique(data):
    sorted_data = sorted(data)
    prev = sorted_data[0]
    for e in xrange(1,len(sorted_data)):
        if prev == sorted_data[e]:
            return false
        prev = sorted_data[e]
    return True

class TestUnique(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(isunique("senthil"),True)

if __name__ == "__main__":
    unittest.main() 



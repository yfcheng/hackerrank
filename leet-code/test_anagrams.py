import unittest

from anagrams import Solution


class MyTest(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.anagrams(["cat","dog","tac","god"]), ["cat","tac","dog","god"])

if __name__ == "__main__":
    unittest.main()

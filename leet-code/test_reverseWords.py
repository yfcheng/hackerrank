import unittest

from reverseWords import Solution


class MyTest(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.reverseWords("hello World"), "World hello")
        self.assertEqual(sol.reverseWords(""), "")
        self.assertEqual(sol.reverseWords("hell !! 77 && world "), "world && 77 !! hell")
        self.assertEqual(sol.reverseWords("   a   b  "), "b a")


if __name__ == "__main__":
    unittest.main()

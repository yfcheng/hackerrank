import unittest

from isPalindromeNumber import Solution


class MyTest(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(100000), False)
        self.assertEqual(sol.isPalindrome(1001), True)
        self.assertEqual(sol.isPalindrome(0), True)
        self.assertEqual(sol.isPalindrome(-2), False)
        self.assertEqual(sol.isPalindrome(5), True)
        self.assertEqual(sol.isPalindrome(16461), True)
        self.assertEqual(sol.isPalindrome(164461), True)
        self.assertEqual(sol.isPalindrome(164361), False)
        self.assertEqual(sol.isPalindrome(2147447412), True)
        self.assertEqual(sol.isPalindrome(-2147447412), False)
        self.assertEqual(sol.isPalindrome(1000021), False)

if __name__ == "__main__":
    unittest.main()

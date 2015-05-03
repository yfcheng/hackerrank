import unittest

from reverseInteger import Solution


class MyTest(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.reverse(100000), 1)
        self.assertEqual(sol.reverse(1001), 1001)
        self.assertEqual(sol.reverse(0), 0)
        self.assertEqual(sol.reverse(-2), -2)
        self.assertEqual(sol.reverse(123), 321)
        self.assertEqual(sol.reverse(-123), -321)
        self.assertEqual(sol.reverse(1000000003), 0)

if __name__ == "__main__":
    unittest.main()

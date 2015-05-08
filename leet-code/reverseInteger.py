"""
Reverse digits of an integer.
    Example1: x = 123, return 321
    Example2: x = -123, return -321
https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x > -10 and x < 10:
            return x
        y = (x * -1) if (x < 0) else x 
        num = y
        pow = 0
        while num > 9:
            pow += 1
            num /= 10
        reverse = 0
        num = y
        while pow > 0:
            reverse += (num % 10)
            num /= 10
            reverse *= 10
            pow -= 1
        reverse += num
        reverse = (reverse * -1) if (x < 0) else reverse
        reverse = 0 if (reverse > 2147483647) else reverse
        reverse = 0 if (reverse < -2147483647) else reverse
        return reverse

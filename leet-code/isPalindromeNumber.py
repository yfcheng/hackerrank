#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x):
        if x > -1 and x < 10:
            return True
        if x < 0:
            return False
        pow = 0
        num = x
        while num > 9:
            pow += 1
            num /= 10
        right = x
        #print pow,x 
        while right > 9:
            if (right % 10) != (right / (10 ** pow)):
                return False
            right /= 10
            pow -= 1
            right = right % (10 ** pow)
            pow -= 1
        if pow > 1 and right != 0:
            return False
        return True

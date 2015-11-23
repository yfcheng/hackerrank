"""

Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length. 

https://leetcode.com/problems/remove-element/

"""

class Solution(object):
    def removeElement(self, nums, val):
        i, j, k = 0, 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        while k < (i - j):
            nums.pop()
            k += 1
        return j


import unittest
from ddt import ddt, data, file_data, unpack
@ddt
class RemoveElementTestCase(unittest.TestCase):
    @unpack
    @data({'nums' : [1,2,3,4,5,2], 'val' : 2, 'expected' : 4},
        {'nums' : [4,5], 'val' : 4, 'expected' : 1})
    def test_inputs(self, nums, val, expected):
        sol = Solution()
        self.assertEqual(sol.removeElement(nums, val), expected)

if __name__ == '__main__':
    unittest.main()
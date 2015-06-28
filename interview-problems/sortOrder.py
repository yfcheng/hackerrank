"""
Sort an array such that odd numbers are in front of even numbers and their relative order does not change.
"""
import unittest

def sortOrder(nums):
    if nums is None or len(nums) == 0:
        return nums
    i,j = 0,0
    while i < len(nums) and j < len(nums):
        while nums[i] % 2 != 0:     #find the index of even number
            i += 1
        while nums[j] % 2 == 0:     #find the index of odd number
            j += 1
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j += 1
    return nums


class SortOrderTest(unittest.TestCase):
    def testSortOrder(self):
        self.assertEqual(sortOrder([]),[])
        self.assertEqual(sortOrder([2,3,5,9,4,6,8,7]),[3,5,9,7,2,4,6,8])
        self.assertEqual(sortOrder([2,9,4,6,8,7]),[9,7,2,4,6,8])

if __name__ == "__main__":
    unittest.main()

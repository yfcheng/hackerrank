"""
moveAllEvensToLeft(new int[]{1, 4, 3, 4, 3, 4, 1, 4, 1, 3, 5, 6});
moveAllEvensToLeft(new int[]{1, 4, 4, 6});
moveAllEvensToLeft(new int[]{4, 4, 6, 1});
moveAllEvensToLeft(new int[]{4, 3, 4, 6, 1});
moveAllEvensToLeft(new int[]{1, 3, 4});
moveAllEvensToLeft(new int[]{1, 4});
"""

def allEvenToLeftOddToRight(nums):
    odd, even,i = 0,0,0
    while i < len(nums):
        if nums[i] % 2 == 1:
            odd = i
        else:
            even = i;
        i += 1
    return nums


input = [12, 34, 45, 9, 8, 90, 3]
output = [12, 34, 8, 90, 45, 9, 3]
print allEvenToLeftOddToRight(input)
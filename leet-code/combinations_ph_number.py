"""

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
             return []

        phNumDict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        res = []
        out = []
        numbers = list(digits)

        for digit in numbers:
            if digit in phNumDict:
                res = phNumDict[ digit ]
                if len(out) == 0:
                    out = res
                    continue
                tmp = []
                for r in res:
                    for o in out:
                        tmp.append(o + "" + r)
                out = tmp
        out = sorted(out)
        return out

import unittest
from ddt import ddt, data, file_data, unpack
@ddt
class LetterCombinationsTestCase(unittest.TestCase):
    @unpack
    @data({"digits" : "23", "expected" : ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]},
        {"digits" : "2", "expected" : ["a","b","c"]},
        {"digits" : "" , "expected" : []},
        {"digits" : "8" , "expected" : ["t","u","v"]})
    def test_inputs(self, digits, expected):
        sol = Solution()
        self.assertEqual(sol.letterCombinations(digits), expected)

if __name__ == '__main__':
    unittest.main()

"""
"2" => ["a","b","c"]
"" => []
"""
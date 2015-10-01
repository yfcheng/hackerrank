"""
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def isFound(self, word, wId, board, x, y):
        if wId > len(word)-1:
            return True
 
        if x < 0 or x > (len(board)-1) or y < 0 or y > (len(board[0])-1):
            return False

        if board[x][y] == word[wId]:
            orig = board[x]
            temp = list(board[x])
            temp[y] = "#"
            board[x] = "".join(temp)
            if self.isFound(word, wId+1, board, x-1, y) or self.isFound(word, wId+1, board, x+1, y) or self.isFound(word, wId+1, board, x, y + 1) or self.isFound(word, wId+1, board, x, y - 1):
                return True
            board[x] = orig
        else:
            return False

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if self.isFound(word, 0, board, i, j):
                        return True
        return False


import unittest
from ddt import ddt, data, file_data, unpack
@ddt
class WordSearchTestCases(unittest.TestCase):
    @unpack
    @data({'board' : ["ABCE","SFCS","ADEE"], 'word' : "ABCCED", 'expected' : True},
        {'board' : ["ABCE","SFCS","ADEE"], 'word' : "SEE", 'expected' : True},
        {'board' : ["ABCE","SFCS","ADEE"], 'word' : "ABCB", 'expected' : False},
        {'board' : ["a"], 'word' : "a", 'expected' : True},
        {'board' : ["aa"], 'word' : "aa", 'expected' : True})
    def test_inputs(self, board, word, expected):
        sol = Solution()
        self.assertEqual(sol.exist(board, word), expected)

if __name__ == '__main__':
    unittest.main()

#print(sol.exist( board, "ABCB"))
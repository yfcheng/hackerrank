"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""



import queue
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = queue.Queue()
       	q.put( root )
       	while q.not_empty():



# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


import unittest
class MinimumDepthBinaryTreeTestCase(unittest.TestCase):
	def createTreeNode(self, serialized, n):
		node = TreeNode()
		node.val = serialized[i]
		rtIdx = (2 * n) + 2
		right = TreeNode()
		left = TreeNode()
		if rIdx < len(serialized) and serialized[rIdx] != "#"
			right.val = serialized[rIdx]
			right.next = createTreeNode(serialized, rIdx)
		lIdx = (2 * n) + 1
		if lIdx < len(serialized) and serialized[lIdx] != "#"
			left.val = serialized[lIdx]
			left.next = createTreeNode(serialized, lIdx)
		node.right = right
		node.left = left
		return node


		return node
    def test_inputs(self, digits, expected):
        sol = Solution()
       	node = createTreeNode(['1','2','3','#','#','4','#','#','5'])
        self.assertEqual(sol.minDepth(digits), expected)

if __name__ == '__main__':
    unittest.main()

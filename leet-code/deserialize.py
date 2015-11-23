# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
		
def createTreeNode(serialized, n):
	node = TreeNode()
	node.val = serialized[n]
	r = (2 * n) + 2
	l = (2 * n) + 1
	right = TreeNode()
	left = TreeNode()
	if r < len(serialized) and serialized[r] != "#":
		right.val = serialized[r]
		right.next = createTreeNode(serialized, r)
	if l < len(serialized) and serialized[l] != "#":
		left.val = serialized[l]
		left.next = createTreeNode(serialized, l)
	node.right = right
	node.left = left
	return node
node = createTreeNode(['1','2','3','#','#','4','#','#','5'], 0)
print(node)
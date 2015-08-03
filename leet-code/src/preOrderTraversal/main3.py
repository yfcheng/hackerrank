class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def preorderTraversal(self, root):
        ret = []

        def visit(e):
            ret.append(e.val)

        if root == None:
            return ret
        stack = [root]
        while stack:
            curr = stack.pop()
            visit(curr)
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)

        return ret


def makeTree(A, i):
    if i >= len(A):
        return None
    node = TreeNode(A[i])
    # print node.val,
    node.left = makeTree(A, i * 2 + 1)
    node.right = makeTree(A, i * 2 + 2)
    return node

if __name__ == '__main__':
    t = [1, 2, 5, 3, 4, 0, 6]
    root = makeTree(t, 0)
    s = Solution()
    for e in s.preorderTraversal(root):
        print e,

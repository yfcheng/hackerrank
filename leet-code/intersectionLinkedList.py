# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        while currA is not None:
            lenA += 1
            currA = currA.next
        while currB is not None:
            lenB += 1
            currB = currB.next
        currA, currB = headA, headB
        if lenA > lenB:
            for i in xrange(lenA - lenB):
                currA = currA.next
        else:
            for i in xrange(lenB - lenA):
                currB = currB.next
        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA
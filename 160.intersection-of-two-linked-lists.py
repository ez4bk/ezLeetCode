#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB:
            if headB in s:
                return headB
            headB = headB.next

        # one = headA
        # two = headB

        # while one != two:
        #     one = headB if one is None else one.next
        #     two = headA if two is None else two.next
        # return one


# @lc code=end

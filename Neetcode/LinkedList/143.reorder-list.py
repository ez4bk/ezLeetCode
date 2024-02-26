#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        In plcae reordering as required.
        1. Use slow and fast pointers to find the mid-node of the LL
        2. Split the LL into two LLs
        3. Reverse the second half
        4. Merge the two LLs
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        midPoint = slow.next
        slow.next = None
        
        # Reverse the second half
        prev = None
        curr = midPoint
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        p1 = head
        p2 = prev
        while p2:
            n1 = p1.next
            n2 = p2.next
            p1.next = p2
            p2.next = n1
            p1 = n1
            p2 = n2
        
        
# @lc code=end


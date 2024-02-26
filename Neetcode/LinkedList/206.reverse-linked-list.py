#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Firstly I think of using a stack and two while loops.
        But then I found this approach that is smarter and faster.
        Use a prev pointer referring the previous node in traversal.
        Link each node to its previous node. Done.
        """
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
# @lc code=end

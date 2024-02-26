#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Originally traversing the entire LL to find the number of elements of it,
        and then traverse again to eliminate the (len - n + 1)th element. Leading to O(2n).
        
        Now use two pointers to find the (n + 1)th node from the end of the list.
        First one goes to (n + 1)th element. Then the second one starts from the begining,
        both start traversing until the first one reaches the end.
        The the second pointer will be pointing at (n + 1)th node from the end of the list.
        """
        dummy = ListNode(-1, head)
        k = n + 1
        p1 = dummy
        for _ in range(k):
            p1 = p1.next
        p2 = dummy
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        
        return dummy.next
# @lc code=end


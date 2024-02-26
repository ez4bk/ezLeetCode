#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Compare values from the two LLs using two pointers, push the smaller one
        to the result LL.
        Don't forget to check for remaining nodes after the loop as the loop ends
        when one of the LLs ends.
        """
        head = ListNode()
        ptr1 = list1
        ptr2 = list2
        
        node = head
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                node.next = ptr1
                ptr1 = ptr1.next
            else:
                node.next = ptr2
                ptr2 = ptr2.next
            node = node.next
        
        if ptr1:
            node.next = ptr1
        if ptr2:
            node.next = ptr2
            
        return head.next
                
        
# @lc code=end


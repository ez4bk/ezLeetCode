#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        """
        Originally using a set and find duplicate during traversal.
        Now using a slow pointer traversing one by one and a fast pointer
        traversing by two steps in each interation.
        
        If the fast pointer meet the slow pointer, then cycle exists.
        Otherwise, the fast pointer would've reached the end in O(n/2) time.
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False


# if __name__ == '__main__':
#     node0 = ListNode(3)
#     node1 = ListNode(2)
#     node2 = ListNode(0)
#     node3 = ListNode(-4)
#     node0.next = node1
#     node1.next = node2
#     node2.next = node3
#     node3.next = node1
#     sol = Solution()
#     print(sol.hasCycle(node0))

# @lc code=end

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
        # stack = {}
        # while head:
        #     if head.next in stack:
        #         return True
        #     else:
        #         stack[head] = True
        #         head = head.next

        # return False
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

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

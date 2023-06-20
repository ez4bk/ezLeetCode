#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        import collections
        dic = collections.defaultdict(lambda: Node(0))
        dic[None] = None
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]

        # @lc code=end
# if __name__ == '__main__':
#     node4 = Node(1)
#     node3 = Node(10, node4)
#     node2 = Node(11, node3, node4)
#     node1 = Node(13, node2)
#     node0 = Node(7, node1, None)
#     node1.random = node0
#     node3.random = node2
#     node4.random = node0
#     sol = Solution()
#     sol.copyRandomList(node0)

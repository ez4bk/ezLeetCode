#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    Use priority queue and heap sort. (heapq in python)
    heapq.heappush(pq, (node.val, id(node), node)) works in the way that:
        heapq will push the tuple in to pq by comparing the tuple with elements
        in pq using < and <= operation.
        (You can override __lt__ and __le__ in ListNode to simply heappush(pq, node))
        Dealing with tuple, it will compare the first element as the key.
        But we sometimes end up having the same priority for some nodes, then it compares
        the second element in the tuple, which is why we need a id(node) which is unique
        for each node. (Though problem will occur for identical nodes.)
    Note: if we push all nodes in to the priority queue, the time complexity
    for pushing will be O(m*n).
    Thus, push all heads only in lists into the priority queue since each LL is sorted.
    Pop the root into the result LL and push the next node of it in its original LL to
    the priority queue.
    
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        pq = []
        
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, id(head), head))
                
        
        while pq:
            node = heapq.heappop(pq)[2]
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, id(node.next), node))
            p = p.next
        
        return dummy.next
        
# @lc code=end


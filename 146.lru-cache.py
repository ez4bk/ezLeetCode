#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key=-1, value=-1, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.nodeTable = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.nodeTable:
            node = self.nodeTable[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.nodeTable.get(key):
            self._remove(self.nodeTable[key])

        node = Node(key, value)
        self._add_to_tail(node)
        self.nodeTable[key] = node

        if len(self.nodeTable) > self.capacity:
            temp = self.head.next
            self._remove(temp)
            del self.nodeTable[temp.key]

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add_to_tail(self, node):
        tail = self.tail.prev
        tail.next = node
        self.tail.prev = node
        node.prev = tail
        node.next = self.tail
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    # @lc code=end

#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#


# @lc code=start
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1
        if not self.head:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.addAtHead(val)
            return
        curr = self.head
        for _ in range(self.length - 1):
            curr = curr.next
        curr.next = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        if not self.head:
            self.addAtHead(val)
            return
        node = ListNode(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next, node.next = node, curr.next
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index > self.length - 1:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

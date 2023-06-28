#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#


# @lc code=start
class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.head = None

    def put(self, key: int, value: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        curr = dummy
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                # self.print_all()
                return
            curr = curr.next

        node = ListNode(key, value)
        curr.next = node
        self.head = dummy.next
        # self.print_all()

    def get(self, key: int) -> int:
        dummy = ListNode()
        dummy.next = self.head
        curr = dummy
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        curr = dummy
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            else:
                curr = curr.next
        self.head = dummy.next
        # self.print_all()

    # def print_all(self):
    #     res = []
    #     dummy = ListNode()
    #     dummy.next = self.head
    #     curr = dummy
    #     while curr.next:
    #         a = [curr.next.key, curr.next.val]
    #         res.append(a)
    #         curr = curr.next
    #     print(res)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

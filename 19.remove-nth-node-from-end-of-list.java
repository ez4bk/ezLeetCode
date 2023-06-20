/*
 * @lc app=leetcode.cn id=19 lang=java
 *
 * [19] Remove Nth Node From End of List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode tail = head;
        int length = 0;
        while (tail != null) {
            length++;
            tail = tail.next;
        }

        if (length == n) {
            head = head.next;
            return head;
        }
        ListNode node = head;
        for (int i = 1; i < length - n; i++) {
            node = node.next;
        }

        node.next = node.next.next;

        return head;

    }
}
// @lc code=end

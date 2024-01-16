/*
 * @lc app=leetcode.cn id=24 lang=java
 *
 * [24] Swap Nodes in Pairs
 */

// @lc code=start
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode node = head;

        while (node != null && node.next != null) {
            node.next = node.next.next;
            node.next.next = node;
            node = node.next.next;
        }

        return head;
    }
}
// @lc code=end

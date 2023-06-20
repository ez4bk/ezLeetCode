/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] Merge k Sorted Lists
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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null) {
            return null;
        }

        ListNode mList = null;
        for (ListNode listNode : lists) {
            mList = merge2Lists(mList, listNode);
        }
        return mList;

    }

    private ListNode merge2Lists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        } else if (list2 == null) {
            return list1;
        } else if (list1.val < list2.val) {
            list1.next = merge2Lists(list1.next, list2);
            return list1;
        } else {
            list2.next = merge2Lists(list1, list2.next);
            return list2;
        }
    }

}
// @lc code=end

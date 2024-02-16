/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        // String y = new String(Integer.toString(x));
        // int lpt = 0;
        // int rpt = y.length() - 1;
        // while (lpt < rpt) {
        // if (y.charAt(lpt) != y.charAt(rpt)) {
        // return false;
        // }
        // lpt++;
        // rpt--;
        // }
        // return true;
        int temp = x;
        int reverse = 0;
        while (temp > 0) {
            int last_digit = temp % 10;
            temp = temp / 10;
            reverse = reverse * 10 + last_digit;
        }
        return reverse == x;
    }
}
// @lc code=end

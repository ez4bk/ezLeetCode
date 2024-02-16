/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> valToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int theOther = target - nums[i];
            if (valToIndex.containsKey(theOther)) {
                return new int[] { valToIndex.get(theOther), i };
            }
            valToIndex.put(nums[i], i);
        }
        return new int[0];
    }
}
// @lc code=end

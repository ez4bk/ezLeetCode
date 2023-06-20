#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        prev2 = 1
        prev1 = 1

        for i in range(2, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1

# @lc code=end

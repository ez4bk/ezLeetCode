#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0]
        for i in range(1, n+1):
            count.append(count[i >> 1] + (i & 1))
        return count
# @lc code=end

#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = {}
        for i, num in enumerate(nums):
            if a.get(num) is not None:
                if i - a[num] <= k:
                    return True
            a[num] = i
        return False


# @lc code=end

#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Tricky one. Kinda like the idea of DP.
        We track of the prefix product of an element i from the
        beginning as well as the postfix product from the end.
        And when their indices go across, prefix * postfix is
        automatically done.
        """
        n = len(nums)
        res = [1] * n
        pre = 1
        post = 1
        
        for i in range(n):
            res[i] *= pre
            pre *= nums[i]
            res[n-1-i] *= post
            post *= nums[n-1-i]
        
        return res

# @lc code=end


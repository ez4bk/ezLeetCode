#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        length = len(nums)

        nums.sort()

        for i in range(length):
            if nums[i] > 0 and nums[i] < nums[i-1]:
                continue
            m = i + 1
            e = length - 1
            while m < e:
                s = nums[i]+nums[m]+nums[e]
                if s < 0:
                    m += 1
                elif s > 0:
                    e -= 1
                else:
                    temp = [nums[i], nums[m], nums[e]]
                    if temp not in r:
                        r.append(temp)
                    m += 1

        return r

# @lc code=end

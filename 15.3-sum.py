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
            if nums[i] > 0 and nums[i] < nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum < 0:
                    left += 1
                elif curSum > 0:
                    right -= 1
                else:
                    temp = [nums[i], nums[left], nums[right]]
                    if temp not in r:
                        r.append(temp)
                    left += 1

        return r


# @lc code=end

#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        minGap = float("inf")
        res = 0

        nums.sort()

        for i in range(length):
            # if nums[i] > 0 and nums[i] < nums[i - 1]:
            #     continue
            left = i + 1
            right = length - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum < target:
                    left += 1
                    if abs(curSum - target) < minGap:
                        minGap = abs(curSum - target)
                        res = curSum
                elif curSum > target:
                    right -= 1
                    if abs(curSum - target) < minGap:
                        minGap = abs(curSum - target)
                        res = curSum
                else:
                    return target
        return res


# @lc code=end

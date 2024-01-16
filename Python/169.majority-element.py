#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        if n == 1:
            return nums[0]

        for num in nums:
            if not dic.get(num):
                dic[num] = 1
            else:
                dic[num] += 1
                if dic[num] > n // 2:
                    return num


# @lc code=end

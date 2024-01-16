#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        if len(nums) == 1:
            return [str(nums[0])]

        lower = nums[0]
        upper = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                upper = nums[i]
            else:
                if lower == upper:
                    res.append(str(lower))
                else:
                    res.append(str(lower) + "->" + str(upper))
                lower = nums[i]
                upper = nums[i]

        if lower == upper:
            res.append(str(lower))
        else:
            res.append(str(lower) + "->" + str(upper))
        return res


# @lc code=end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Most common solutions for string problems are done using
        Set() or Dict().
        Use dict to record the mapping of
            (Difference of A[i] and target): i
        When another value A[j] matches a key in the dict, return.
        """
        
        valToIndex = {}
        for i in range(len(nums)):
            if nums[i] in valToIndex:
                return [i, valToIndex[nums[i]]]
            else:
                delta = target - nums[i]
                valToIndex[delta] = i
        
# @lc code=end


#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#


# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        comp = set(range(1, len(nums) + 1))
        for n in nums:
            if n in comp:
                comp.remove(n)
        return list(comp)


# @lc code=end

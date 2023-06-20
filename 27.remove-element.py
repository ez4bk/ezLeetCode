#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = []
        for key in nums:
            if key != val:
                a.append(key)
        nums[:] = a
        return len(a)


# @lc code=end

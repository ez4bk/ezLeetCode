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
        n = len(nums)
        res = set()
        
        nums.sort()

        for i in range(n-2):
            # if i > 0 and nums[i] == nums[i+1]:
            #     continue
            lo = i + 1
            hi = n - 1
            while lo < hi:
                temp = (nums[i], nums[lo], nums[hi])
                sumTemp = sum(temp)
                if sumTemp < 0:
                    lo += 1
                elif sumTemp > 0:
                    hi -= 1
                else:
                    res.add(temp)
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        return list(res)
        
                            
print(Solution().threeSum([-4, -1, -1, 0, 1, 2]))
# @lc code=end

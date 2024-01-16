#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window approach O(n)
        # res = float("inf")
        # sum = 0
        # start = 0
        # subLen = 0
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     while sum >= target:
        #         subLen = i - start + 1
        #         if res >= subLen:
        #             res = subLen
        #         sum -= nums[start]
        #         start += 1
        # return 0 if res == float("inf") else res

        # Binary search for end position for each start position
        # sum = 0
        # minLen = float("inf")
        # sums = [0] * len(nums)
        # for i in range(len(sums)):
        #     sums[i] = nums[i] + (0 if i == 0 else sums[i - 1])

        # for i in range(len(nums)):
        #     j = self.findWindowEnd(i, sums, target)
        #     if j == len(nums):
        #         break
        #     minLen = min(j - i + 1, minLen)

        # return 0 if minLen == float("inf") else minLen

        # Binary search for a window of size k that satisfies
        left = 1
        right = len(nums)
        minLen = 0
        while left <= right:
            mid = (left + right) // 2
            if self.windowExist(mid, nums, target):
                right = mid - 1
                minLen = mid
            else:
                left = mid + 1

        return minLen

    def windowExist(self, size, nums, s):
        sum = 0
        for i in range(len(nums)):
            if i >= size:
                sum -= nums[i - size]
            sum += nums[i]
            if sum >= s:
                return True
        return False

    def findWindowEnd(self, start, sums, s):
        left = start
        right = len(sums) - 1
        offset = 0 if start == 0 else sums[start - 1]

        while left <= right:
            mid = (left + right) // 2
            sum = sums[mid] - offset
            if sum >= s:
                right = mid - 1
            else:
                left = mid + 1
        return left


# @lc code=end

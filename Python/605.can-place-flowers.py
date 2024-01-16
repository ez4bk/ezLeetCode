#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#


# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0:
                if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0


print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))

# @lc code=end

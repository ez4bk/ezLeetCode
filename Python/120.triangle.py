#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#


# @lc code=start
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                triangle[i][j] += min(
                    triangle[i - 1][j - 1] if j > 0 else float("inf"),
                    triangle[i - 1][j] if j < i else float("inf"),
                )
        return min(triangle[-1])


print(Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]]))
# @lc code=end

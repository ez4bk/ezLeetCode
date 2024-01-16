#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        traverse = [row[:] for row in matrix]
        for i in range(0, len(traverse)):
            for j in range(0, len(traverse[i])):
                if traverse[i][j] == 0:
                    for m in range(0, len(matrix)):
                        matrix[m][j] = 0
                    for n in range(0, len(matrix[i])):
                        matrix[i][n] = 0
# @lc code=end

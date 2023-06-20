#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # import numpy as np
        # matrix[:] = np.fliplr(np.transpose(matrix))

        n = len(matrix)
        depth = n // 2
        for i in range(depth):
            sidelen, opp = n - 2 * i - 1, n - 1 - i
            for j in range(sidelen):
                temp = matrix[i][i+j]
                matrix[i][i+j] = matrix[opp-j][i]
                matrix[opp-j][i] = matrix[opp][opp-j]
                matrix[opp][opp-j] = matrix[i+j][opp]
                matrix[i+j][opp] = temp

# @lc code=end

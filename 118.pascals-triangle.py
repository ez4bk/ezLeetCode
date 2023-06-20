#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        curr = [1]
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(numRows - 1):
            temp = [0] + curr + [0]
            curr = []
            for j in range(len(temp) - 1):
                curr.append(temp[j] + temp[j + 1])
            res.append(curr)
        return res


# @lc code=end

#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n] * n
        startx, starty = 0, 0
        loop = n // 2
        mid = n // 2
        count = 1
        offset = 1
        while loop:
            i = startx
            j = starty
            for j in range(starty, starty + n - offset):
                res[startx][j] = count
                count += 1
            for i in range(startx, startx + n - offset):
                res[i][j] = count
                count += 1
            for j in range(j, starty, -1):
                res[i][j] = count
                count += 1
            for i in range(i, startx, -1):
                res[i][j] = count
                count += 1
            startx += 1
            starty += 1
            offset += 2

        if n % 2:
            res[mid][mid] = count
        return res


# @lc code=end

#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#


# @lc code=start
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        score_board = []
        for op in operations:
            if op == "+":
                score_board.append(score_board[-1] + score_board[-2])
            elif op == "D":
                score_board.append(score_board[-1] * 2)
            elif op == "C":
                score_board.pop()
            else:
                score_board.append(int(op))

        return sum(score_board)


# @lc code=end

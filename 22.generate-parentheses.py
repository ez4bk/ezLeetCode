#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        res = ["()"]
        for i in range(n - 1):
            temp = set()
            for p in res:
                for j in range(len(p)):
                    temp.add(p[:j] + "()" + p[j:])
            res = temp
        return res


# @lc code=end

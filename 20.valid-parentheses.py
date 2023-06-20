#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:

    def isValid(self, s: str) -> bool:
        parenthese = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        string = [*s]
        sol = []
        for a in string:
            # print(sol)
            if parenthese.get(a):
                sol.append(a)
            else:
                if len(sol) < 1:
                    sol.append(a)
                elif parenthese.get(sol[-1]) == a:
                    sol.pop()
                else:
                    sol.append(a)

        return sol == []
        print(sol)

# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    solution.isValid('(])')

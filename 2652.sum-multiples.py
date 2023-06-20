#
# @lc app=leetcode id=2652 lang=python3
#
# [2652] Sum Multiples
#

# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def algo(x): return x*(x+1)//2
        return algo(n//3)*3 + algo(n//5)*5 + algo(n//7)*7 - algo(n//15)*15 - algo(n//21)*21 - algo(n//35)*35 + algo(n//105)*105

# @lc code=end

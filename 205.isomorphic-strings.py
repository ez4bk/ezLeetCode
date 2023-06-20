#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a, b = {}, {}
        for i, j in zip(s, t):
            if i not in a:
                a[i] = j
            if j not in b:
                b[j] = i
            if a[i] != j or b[j] != i:
                return False
        return True


# @lc code=end

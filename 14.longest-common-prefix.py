#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(a) != 0:
                a = a[:-1]
        return a
# @lc code=end

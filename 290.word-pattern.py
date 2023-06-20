#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(" ")
        pat = {}
        pattern = list(pattern)

        if len(pattern) != len(ss):
            return False

        for i in range(len(pattern)):
            if not pat.get(pattern[i]):
                if ss[i] in pat.values():
                    return False
                else:
                    pat[pattern[i]] = ss[i]
            else:
                if pat[pattern[i]] != ss[i]:
                    return False
        return True


Solution().wordPattern("abba", "dog cat cat dog")
# @lc code=end

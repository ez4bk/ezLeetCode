#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mdict = {}
        for m in magazine:
            if m in mdict:
                mdict[m] += 1
            else:
                mdict[m] = 1
        for r in ransomNote:
            if r not in mdict or mdict[r] <= 0:
                return False
            mdict[r] -= 1
        return True


# @lc code=end

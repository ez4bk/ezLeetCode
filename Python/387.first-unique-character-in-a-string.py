#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i in count:
            if count[i] == 1:
                return s.index(i)

        return -1
# @lc code=end

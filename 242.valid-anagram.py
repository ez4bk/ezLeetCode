#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tracker = collections.defaultdict(int)
        for x in s:
            tracker[x] += 1
        for x in t:
            tracker[x] -= 1
        return all(x == 0 for x in tracker.values())

# @lc code=end

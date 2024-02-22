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
        count_s = self.encode(s)
        count_t = self.encode(t)
        for i in range(len(count_s)):
            if count_s[i] != count_t[i]:
                return False
        return True
    
    def encode(self, s):
        """
        !!! The main idea is here. Encode each string to
        a list counting the occurrences for each letter.
        
        Each type of anagram should have the same result.
        """
        count = [0] * 26
        for c in s:
            delta = ord(c) - ord('a')
            count[delta] += 1
        return count

# @lc code=end

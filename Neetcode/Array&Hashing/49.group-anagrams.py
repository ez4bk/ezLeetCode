#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        We encode each element. Same anagram should have the same
        encoding. And we use a dict to record a mapping of:
            (A type of encoding): (Elements having the same encoding)
        """
        codeToList = {}
        for item in strs:
            code = self.encode(item)
            if not codeToList.get(code):
                codeToList[code] = []
            codeToList[code].append(item)
        res = []
        for l in codeToList.values():
            res.append(l)
        return res
    
    def encode(self, s):
        """
        Same idea as 242. But this time we return a stringfied list.
        """
        count = [0] * 26
        for c in s:
            delta = ord(c) - ord('a')
            count[delta] += 1
        return str(count)
# @lc code=end

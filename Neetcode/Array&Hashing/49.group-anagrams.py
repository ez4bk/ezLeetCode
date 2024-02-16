#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
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
        count = [0] * 26
        for c in s:
            delta = ord(c) - ord('a')
            count[delta] += 1
        return str(count)
# @lc code=end

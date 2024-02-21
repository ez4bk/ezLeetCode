#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

class Solution:

    def encode(self, strs: List[str]) -> str:
        enStr = ""

        for s in strs:
            temp = str(len(s)) + "#" + s
            enStr += temp
        
        return enStr
        
    def decode(self, s: str) -> List[str]:
        deStrs = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            deStrs.append(s[i:j])
            i = j
        
        return deStrs

# @lc code=end
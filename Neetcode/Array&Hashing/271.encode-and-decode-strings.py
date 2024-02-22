#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Either str(len(s)) + "#" + s or s + "#" + str(len(s))
        would work. But considering the ease of decoding, the prior
        one is better.
        """
        enStr = ""

        for s in strs:
            temp = str(len(s)) + "#" + s
            enStr += temp
        
        return enStr
        
    def decode(self, s: str) -> List[str]:
        """
        Anything before "#" must be an integer representing the length
        of the next string element. Using this number we can extract the
        actuall string element from the whole string.
        """
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
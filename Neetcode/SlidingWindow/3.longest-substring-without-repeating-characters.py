#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Originally use a set to detect duplicate characters. When found duplicated,
        clear the set and move the left side by ONE only, leading to O(n^2).
        Then I tried to use a dictionary to record the index of each character. When
        dulicated keys detected, set the left side to dict[key] + 1 and clear the dict, 
        which cuased some edge issues.
        
        The current implementation uses a dictionary to record occurencies, and shrink
        the left side accordingly to maintain the occurence of each character to 
        not exceeding 1. During shrinking, also update occurence that's beed left out to
        the left side of the left pointer. 
        """
        window = {}
        left = right = 0
        res = 0
        
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right-left)
        return res
# @lc code=end


#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Increment right pointer to expand the result substring,
        record the frequencies of chars within the window,
        dynamically calculate the replacement cost:
            count the number of elements in between left and right pointers,
            subtract using the number of most frequent character,
            compare with k
        If replacement cost <= k, then we can continue expand the right pointer,
        otherwise, we shrink the left pointer and update the frequency.
        """
        c_frequency = {}
        left = right = 0
        res = 0
        
        while right < len(s):
            c = s[right]
            right += 1
            c_frequency[c] = c_frequency.get(c, 0) + 1
            
            count = right - left
            if count - max(c_frequency.values()) <= k:
                res = max(res, count)
            else:
                c_frequency[s[left]] -= 1
                if not c_frequency[s[left]]:
                    c_frequency.pop(s[left])
                left += 1
        
        return res
# @lc code=end


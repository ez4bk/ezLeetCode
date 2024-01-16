#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        str = ""
        for c in s:
            if c.isalnum():
                str += c
        str = list(str)
        left = 0
        right = len(str) - 1
        while left <= right:
            if str[left] != str[right]:
                return False
            left += 1
            right -= 1
        return True


# @lc code=end

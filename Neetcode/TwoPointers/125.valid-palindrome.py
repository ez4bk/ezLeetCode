#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Traversing using two pointers from left most and right most towards intersection.
        """
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left <= right:
            while not s[left].isalnum() and left + 1 <= right:
                left += 1
            while not s[right].isalnum() and left <= right - 1:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

Solution().isPalindrome("A man, a plan, a canal: Panama")

# @lc code=end

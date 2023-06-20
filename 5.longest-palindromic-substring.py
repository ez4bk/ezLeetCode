#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    # not really understood
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s

        maxLen = 1
        begin = 0
        dp = [[False for col in range(length)] for row in range(length)]

        for k in range(length):
            dp[k][k] = True

        for j in range(1, length):
            for i in range(0, j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if (j-i) < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and (j - i + 1 > maxLen):
                    maxLen = j - i + 1
                    begin = i

        return s[begin: begin + maxLen]
# @lc code=end

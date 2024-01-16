#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * len(s)
        for i in range(0, len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and (dp[i-len(word)] or i-len(word) == -1):
                    dp[i] = True

        return dp[-1]
        # @lc code=end


if __name__ == '__main__':
    sol = Solution()
    # print(sol.wordBreak('leetcode', ['leet', 'code']))
    # print(sol.wordBreak('applepenapple', ['apple', 'pen']))
    # print(sol.wordBreak('catsandog', ['cat', 'sand', 'and', 'dog', 'cat']))
    print(sol.wordBreak('abcd', ["a", "abc", "b", "cd"]))

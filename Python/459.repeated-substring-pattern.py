#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            if len(s) % i == 0:
                pattern = s[:i]
                temp = s
                for i in range(int(len(temp) / i)):
                    if temp.removeprefix(pattern) != temp:
                        temp = temp.removeprefix(pattern)
                if len(temp) == 0:
                    return True

        return False
# @lc code=end


# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.repeatedSubstringPattern('abcabcabcabc'))

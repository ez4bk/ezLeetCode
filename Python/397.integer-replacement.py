#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        counter = 0
        while n > 1:
            counter += 1
            if n % 2 == 0:
                n = n//2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return counter
# @lc code=end


if __name__ == "__main__":
    a = Solution()
    print(a.integerReplacement(1234))

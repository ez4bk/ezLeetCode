#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = [0]
        for i in range(1, 2**n):
            res.append(res[-1] ^ (i & -i))
        return res


# if __name__ == '__main__':
#     sol = Solution()
#     a = sol.grayCode(4)
#     for i in range(len(a)):
#         print(bin(a[i]).format())
    # @lc code=end

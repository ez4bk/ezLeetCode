#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        cur = [1]
        for i in range(rowIndex):
            temp = [0] + cur + [0]
            cur = []
            for j in range(0, len(temp) - 1):
                cur.append(temp[j] + temp[j+1])

        return cur

    # Bug when submitting
    # def recur(self, target, prev=[1], curIndex=0) -> list[int]:
    #     if curIndex == target:
    #         return prev
    #     else:
    #         prev[:0] = [0]
    #         prev.append(0)

    #         cur = []
    #         for i in range(0, len(prev)-1):
    #             cur.append(prev[i]+prev[i+1])
    #         return self.recur(target, cur, curIndex+1)


# if __name__ == "__main__":
#     s = Solution()
#     print(s.getRow(1))
# @lc code=end

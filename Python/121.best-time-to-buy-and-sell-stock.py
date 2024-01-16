#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyDay = 0
        sellDay = 1
        profit = 0

        while sellDay < len(prices):
            currProfit = prices[sellDay] - prices[buyDay]
            if prices[buyDay] < prices[sellDay]:
                profit = max(profit, currProfit)
            else:
                buyDay = sellDay
            sellDay += 1

        return profit
        # @lc code=end

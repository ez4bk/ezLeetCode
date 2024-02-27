#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        I thought SliDinig Window will be the same idea as those in Two Pointers but no.
        I used to have sellDay pointing to the last day and treated the problem as
        11. Container With Most Water
        But the problem is, in what condition should I move the buyDay or the sellDay.
        So in Sliding Window, you really need to initialize the windows size to 1 in the
        beginning and slide, expand, or shrink the window during the process.
        """
        buyDay = 0
        sellDay = 1
        maxProfit = 0
        while sellDay < len(prices):
            if prices[buyDay] < prices[sellDay]:
                maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])
            else:
                buyDay = sellDay
            sellDay += 1
        return maxProfit
        # @lc code=end

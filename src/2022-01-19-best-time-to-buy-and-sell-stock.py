
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        for i, p in enumerate(prices):
            if i == 0:
                buy = p
                sell = p
                tmp = p
            else:
                if p - tmp > sell - buy:
                    buy = tmp
                    sell = p
                elif p > sell:
                    sell = p
                elif tmp > p:
                    tmp = p

        return sell - buy


s = Solution()

assert s.maxProfit([4, 7, 1, 2, 11]) == 10
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([7, 6, 4, 3, 1]) == 0


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


class Solution2:
    def maxProfit(self, prices):
        buy = sell = tmp = prices[0]
        for p in prices[1:]:
            if p - tmp > sell - buy:
                buy = tmp
                sell = p
            elif p > sell:
                sell = p
            elif tmp > p:
                tmp = p
        return sell - buy


s2 = Solution2()
assert s2.maxProfit([4, 7, 1, 2, 11]) == 10
assert s2.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s2.maxProfit([7, 6, 4, 3, 1]) == 0


class Solution3:
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = prices[0]
        for p in prices[1:]:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit


s3 = Solution3()
assert s3.maxProfit([4, 7, 1, 2, 11]) == 10
assert s3.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s3.maxProfit([7, 6, 4, 3, 1]) == 0

# def sol3(prices):
#     max_profit = 0
#     for i, _ in enumerate(prices):
#         for j, _ in enumerate(prices[i:]):
#             profit = prices[j] - prices[i]
#             if profit > max_profit:
#                 max_profit = profit
#     return max_profit


def sol3(prices):
    max_profit = 0
    for i, p1 in enumerate(prices):
        for j, p2 in enumerate(prices[i:]):
            profit = p2 - p1
            if profit > max_profit:
                max_profit = profit

    return max_profit


print(sol3([7, 10, 1, 6]))

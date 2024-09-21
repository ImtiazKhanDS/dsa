# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prefix_min = [0] * n
        prefix_min[0] = prices[0]
        suffix_max = [0] * n
        suffix_max[n - 1] = prices[n - 1]

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], prices[i])

        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], prices[i])

        profit = 0
        for i in range(n):
            profit = max(profit, suffix_max[i] - prefix_min[i])
        return profit


# @leet end


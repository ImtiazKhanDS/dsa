# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # prefix profit array
        # suffix profit array
        # price[3, 3, 5, 0, 0, 3, 1, 4]
        # pmin [3, 3, 3, 0, 0, 0, 0, 0]
        # pref_profit  [0, 0, 2, 0, 0, 3, 1, 4]
        # smax [5, 5, 5, 4, 4, 4, 4, 4]
        # suff_profit  [2, 2, 0, 4, 4, 1, 3, 0]
        # pre_profit_max : [0, 0, 2, 2, 2, 3, 3, 4]
        # suf_profit_max : [4, 4, 4, 4, 4, 3, 3, 0]
        pmin = [0] * n
        smax = [0] * n
        pmin[0] = prices[0]
        smax[n - 1] = prices[n - 1]

        for i in range(1, n):
            pmin[i] = min(pmin[i - 1], prices[i])

        for i in range(n - 2, -1, -1):
            smax[i] = max(smax[i + 1], prices[i])

        ans = 0
        pref_profit_max = [0] * n
        suffix_profit_max = [0] * n

        pref_profit_max[0] = prices[0] - pmin[0]
        suffix_profit_max[n - 1] = smax[n - 1] - prices[n - 1]

        for i in range(1, n):
            pref_profit_max[i] = max(pref_profit_max[i - 1], prices[i] - pmin[i])

        for i in range(n - 2, -1, -1):
            suffix_profit_max[i] = max(suffix_profit_max[i + 1], smax[i] - prices[i])

        for i in range(n):
            ans = max(pref_profit_max[i] + suffix_profit_max[i], ans)
        return ans


# @leet end


# @leet start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # so create a prefix profit and a suffix profit and then
        # take sum max(ans, prefix_profit + suffix_ profit)
        # prefix profit calculation
        n = len(prices)

        prefix_profit_arr = [0] * n
        prefix_pre_min = prices[0]

        for i in range(1, n):
            prefix_pre_min = min(prefix_pre_min, prices[i])
            prefix_profit_arr[i] = max(
                prefix_profit_arr[i - 1], prices[i] - prefix_pre_min
            )

        suffix_profit_arr = [0] * n
        suffix_suffix_max = prices[n - 1]

        for i in range(n - 2, 0, -1):
            suffix_suffix_max = max(suffix_suffix_max, prices[i])
            suffix_profit_arr[i] = max(
                suffix_profit_arr[i + 1], suffix_suffix_max - prices[i]
            )

        ans = 0
        for i in range(n):
            ans = max(ans, prefix_profit_arr[i] + suffix_profit_arr[i])
        return ans


# @leet end

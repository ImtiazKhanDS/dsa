# @leet start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        prefix_min = [0] * n
        prefix_min[0] = prices[0]
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], prices[i])

        suffix_max = [0] * n
        suffix_max[n - 1] = prices[n - 1]
        for i in range(n - 2, 0, -1):
            suffix_max[i] = max(suffix_max[i + 1], prices[i])

        ans = 0
        for i in range(n):
            ans = max(ans, suffix_max[i] - prefix_min[i])

        return ans


# @leet end

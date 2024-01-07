# @leet start
# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        if not n:
            return ans

        # prefix max calculation
        prefix_max = [0] * n
        prefix_max[0] = height[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])

        # suffix max calculation
        suffix_max = [0] * n
        suffix_max[n - 1] = height[n - 1]
        for i in range(n - 2, 0, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        for i in range(1, n - 1):
            ans += min(prefix_max[i], suffix_max[i]) - height[i]

        return ans


# @leet end

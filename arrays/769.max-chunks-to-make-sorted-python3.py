# @leet start
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_max = [0] * n
        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(arr[i], prefix_max[i - 1])

        ans = 0
        for i in range(n):
            ans += 1 if prefix_max[i] == i else 0

        return ans


# @leet end

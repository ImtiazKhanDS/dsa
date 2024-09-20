# @leet start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_max = [0] * n
        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        ans = 0
        for i in range(n):
            if prefix_max[i] == i:
                ans += 1
        return ans


# @leet end


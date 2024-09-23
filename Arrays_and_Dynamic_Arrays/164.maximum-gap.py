# @leet start
from math import ceil


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_m = max(nums)
        min_m = min(nums)
        gap = ceil((max_m - min_m) / (n - 1))
        if gap == 0:
            return 0
        print(gap, max_m, min_m)
        maxm_arr = [float("-inf")] * n
        minm_arr = [float("inf")] * n

        for i in range(n):
            bucket = ceil((nums[i] - min_m) // gap)
            maxm_arr[bucket] = max(nums[i], maxm_arr[bucket])
            minm_arr[bucket] = min(nums[i], minm_arr[bucket])

        print(maxm_arr)
        print(minm_arr)
        ans = 0
        i = 0
        j = 0
        while i < n and j < n:
            if i == 0 and j == 0:
                i += 1
            if maxm_arr[j] == float("-inf"):
                j += 1

            elif minm_arr[i] == float("inf"):
                i += 1

            else:
                ans = max(ans, minm_arr[i] - maxm_arr[j])
                i += 1
                j += 1

        return ans


# @leet end


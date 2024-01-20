# @leet start
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_ele, min_ele = max(nums), min(nums)
        if max_ele == min_ele:
            return 0

        gap = ceil((max_ele - min_ele) / (n - 1))
        min_bucket = [float("inf") for _ in range(n)]
        max_bucket = [float("-inf") for _ in range(n)]

        for i in range(n):
            bucket_num = (nums[i] - min_ele) // gap
            min_bucket[bucket_num] = min(min_bucket[bucket_num], nums[i])
            max_bucket[bucket_num] = max(max_bucket[bucket_num], nums[i])

        i = 1
        j = 0
        answer = 0
        while j < i and i < n and j < n:
            if min_bucket[i] == float("inf"):
                i += 1
                continue
            if max_bucket[j] == float("-inf"):
                j += 1
                continue
            answer = max(answer, min_bucket[i] - max_bucket[j])
            i += 1
            j += 1
        return answer


# @leet end

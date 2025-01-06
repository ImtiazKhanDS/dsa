# @leet start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix_sum = 0
        _map: dict = {}
        _map[prefix_sum] = 1
        n = len(nums)
        for i in range(n):
            prefix_sum += nums[i]
            if _map.get(prefix_sum - k):
                cnt += _map.get(prefix_sum - k, 0)
            _map[prefix_sum] = _map.get(prefix_sum, 0) + 1
        return cnt


# @leet end


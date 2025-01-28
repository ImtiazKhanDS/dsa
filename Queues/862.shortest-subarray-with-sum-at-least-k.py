# @leet start
from collections import deque
from itertools import accumulate
from math import inf


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sums = list(accumulate(nums, initial=0))

        indices_deque = deque()
        min_length = inf
        for current_index, current_sum in enumerate(prefix_sums):

            while indices_deque and current_sum - prefix_sums[indices_deque[0]] >= k:
                min_length = min(min_length, current_index - indices_deque.popleft())

            while indices_deque and prefix_sums[indices_deque[-1]] >= current_sum:
                indices_deque.pop()

            indices_deque.append(current_index)
        return -1 if min_length == inf else min_length


# @leet end


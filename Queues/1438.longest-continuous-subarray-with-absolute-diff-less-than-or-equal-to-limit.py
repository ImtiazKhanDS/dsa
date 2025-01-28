# @leet start
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue: deque = deque()
        min_queue: deque = deque()

        left = 0
        for el in nums:
            while max_queue and el > max_queue[-1]:
                max_queue.pop()
            max_queue.append(el)

            while min_queue and el < min_queue[-1]:
                min_queue.pop()
            min_queue.append(el)

            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1
        return len(nums) - left


# @leet end


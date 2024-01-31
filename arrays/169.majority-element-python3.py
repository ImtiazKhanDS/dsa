# @leet start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        count = 0
        candidate = nums[0]
        while i < n:
            if count == 0 or i == 0:
                candidate = nums[i]
                count = 1
            elif candidate == nums[i]:
                count += 1
            else:
                count -= 1
            i += 1
        return candidate


# @leet end

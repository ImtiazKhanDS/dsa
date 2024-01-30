# @leet start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        l = len(nums) + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] >= l:
                nums[i] = l

        print("rearranging:", nums)
        for i in range(n):
            if abs(nums[i]) < l:
                k = abs(nums[i]) - 1
                if nums[k] > 0:
                    nums[k] = -nums[k]
        print("negatives:", nums)
        for k in range(n):
            if nums[k] > 0:
                return k + 1
        return n + 1


# @leet end

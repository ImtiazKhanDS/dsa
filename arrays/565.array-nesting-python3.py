# @leet start
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 1
        for i in range(n):
            if nums[i] > 0:
                index = nums[i]
                val = i
                count = 1
                while index != i:
                    temp = nums[index]
                    nums[index] = -(val + 1)
                    val = index
                    index = temp
                    count += 1
                nums[index] = -(val + 1)
                answer = max(answer, count)
        return answer


# @leet end

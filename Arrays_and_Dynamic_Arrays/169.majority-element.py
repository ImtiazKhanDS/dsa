# @leet start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Straight implementation of boyre moores algorithm
        candidate = nums[0]
        count = 1
        n = len(nums)

        for i in range(1, n):
            if candidate != nums[i]:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1
            else:
                count += 1

        return candidate


# @leet end


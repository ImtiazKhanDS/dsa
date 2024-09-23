# @leet start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        l = n + 1

        # Normalize the numbers to l if nums[i] are either negative or greater than or equal to n+1
        for i in range(n):
            if nums[i] >= l or nums[i] <= 0:
                nums[i] = l
        # Use the existing array as a map to make them negative if certain number exists.
        for i in range(n):
            if abs(nums[i]) < l:
                k = abs(nums[i]) - 1
                nums[k] = -abs(nums[k])

        for k in range(n):
            if nums[k] > 0:
                return k + 1
        return l


# @leet end


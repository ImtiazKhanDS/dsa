# @leet start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        # find the break point where first peak appears
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # swap that peak with a number just greater than break point
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
        # arrange the elements after the break point in ascending order so its just greater
        nums[i + 1 :] = reversed(nums[i + 1 :])


# @leet end


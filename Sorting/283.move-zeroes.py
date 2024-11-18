# @leet start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        cnt = 0

        while i < n:
            if nums[i] != 0:
                if i != cnt:
                    nums[i], nums[cnt] = nums[cnt], nums[i]
                cnt += 1
            i += 1
        return nums


# @leet end


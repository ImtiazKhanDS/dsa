# @leet start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n - 1
        if n == 1:
            return 0

        while l <= h:
            m = (l + h) // 2

            if m == 0:
                if nums[m + 1] < nums[m]:
                    return m
                else:
                    l = m + 1
            elif m == n - 1:
                if nums[m - 1] < nums[m]:
                    return m
                else:
                    h = m - 1
            elif nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            elif nums[m - 1] > nums[m]:
                h = m - 1
            else:
                l = m + 1


# @leet end


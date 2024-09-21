# @leet start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < k:
            k = k % n
        for i in range(n // 2):
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]

        print(nums)

        for j in range(k // 2):
            nums[j], nums[k - 1 - j] = nums[k - 1 - j], nums[j]

        print(nums)

        for p in range(k, (n + k + 1) // 2, 1):
            nums[p], nums[n + k - p - 1] = nums[n + k - p - 1], nums[p]


# @leet end


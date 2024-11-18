# @leet start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxm = max(nums) + 1
        cnt = [0] * (maxm)
        for x in nums:
            cnt[x] += 1

        index = 0
        for i in range(maxm):
            while cnt[i] > 0:
                nums[index] = i
                index += 1
                cnt[i] -= 1


# @leet end

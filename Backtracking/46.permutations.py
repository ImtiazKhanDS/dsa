# @leet start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def perm(i: int):
            if i == n:
                ans.append(nums.copy())
                return
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                perm(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        perm(0)
        return ans


# @leet end


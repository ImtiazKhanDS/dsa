# @leet start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def permdup(nums: List[int], i: int, n: int):

            if i == n:
                ans.append(nums.copy())
                return

            freq = [0 for i in range(21)]
            for k in range(i, n):
                if freq[nums[k] + 10] == 0:
                    nums[i], nums[k] = nums[k], nums[i]
                    permdup(nums, i + 1, n)
                    nums[i], nums[k] = nums[k], nums[i]
                    freq[nums[k] + 10] += 1

        permdup(nums, 0, len(nums))
        return ans


# @leet end


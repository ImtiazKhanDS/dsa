# @leet start
class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i + 1 for i in range(n)]
        count = 0

        def permutation(i: int, nums: list):
            nonlocal count
            if i == n:
                count += 1
            for k in range(i, n):
                nums[i], nums[k] = nums[k], nums[i]
                if nums[i] % (i + 1) == 0 or (i + 1) % nums[i] == 0:
                    permutation(i + 1, nums)
                nums[i], nums[k] = nums[k], nums[i]

        permutation(0, nums)
        return count


# @leet end


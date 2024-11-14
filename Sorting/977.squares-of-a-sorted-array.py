# @leet start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pivot = 0
        while pivot < n and nums[pivot] < 0:
            pivot += 1

        def merge(m: int, n: int, nums: list):
            i = m - 1
            j = m
            output = []
            while i >= 0 and j < n:
                if -nums[i] < nums[j]:
                    output.append(nums[i] * nums[i])
                    i -= 1
                else:
                    output.append(nums[j] * nums[j])
                    j += 1
            while i >= 0:
                output.append(nums[i] * nums[i])
                i -= 1
            while j < n:
                output.append(nums[j] * nums[j])
                j += 1

            return output

        return merge(pivot, n, nums)


# @leet end


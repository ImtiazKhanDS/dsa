# @leet start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        visited = [0] * n
        for i in range(n):
            if not visited[i]:
                prev = -1
                curr = i
                count = 0
                while nums[curr] != i:
                    count += 1
                    prev = curr
                    visited[prev] = 1
                    curr = nums[curr]

                if nums[curr] == i:
                    count += 1
                ans = max(ans, count)
        return ans


# @leet end


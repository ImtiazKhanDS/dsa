# @leet start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        mask = 1 << 31
        ans = 0

        while mask:
            cnt = 0
            for i in range(n):
                cnt += 1 if mask & nums[i] else 0
            ans += (n - cnt) * cnt
            mask >>= 1
        return ans


# @leet end


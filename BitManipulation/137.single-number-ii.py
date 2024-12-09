# @leet start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        mask = 1 << 31
        ans = 0
        while mask:
            cnt = 0
            for i in range(n):
                if nums[i] < 0:
                    nums[i] = nums[i] & (2**32 - 1)
                cnt += 1 if mask & nums[i] else 0
            if cnt % 3:
                ans = ans | mask
            mask >>= 1
        if ans >= 2**31:
            ans -= 2**32
        return ans


# @leet end


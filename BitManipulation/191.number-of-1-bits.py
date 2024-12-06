# @leet start
class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1 << 31
        cnt = 0
        while mask:
            if mask & n:
                cnt += 1
            mask >>= 1
        return cnt


# @leet end


# @leet start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        mask = 1 << 31
        ans = 0
        while mask:
            if (mask & left) == (mask & right):
                if mask & left:
                    ans += mask
            else:
                break
            mask >>= 1
        return ans


# @leet end


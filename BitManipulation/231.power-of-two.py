# @leet start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """If n & n-1 (since this flips all bits of n)"""
        return n > 0 and (n & (n - 1)) == 0


# @leet end


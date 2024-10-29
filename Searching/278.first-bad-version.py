# @leet start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        h = n
        while l <= h:
            m = (l + h) // 2

            res = isBadVersion(m)
            if not res:
                res1 = isBadVersion(m + 1)
                if res1:
                    return m + 1
                else:
                    l = m + 1
            else:
                h = m - 1


# @leet end


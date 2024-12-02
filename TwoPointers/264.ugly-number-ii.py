# @leet start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p1, p2, p3 = 0, 0, 0
        arr = [0] * n
        arr[0] = 1
        c = 1
        while c < n:
            val = min([2 * arr[p1], 3 * arr[p2], 5 * arr[p3]])
            arr[c] = val
            if val == 2 * arr[p1]:
                p1 += 1
            if val == 3 * arr[p2]:
                p2 += 1
            if val == 5 * arr[p3]:
                p3 += 1
            c += 1
        return arr[n - 1]


# @leet end


# @leet start
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def rec(k: int, n: int, l: list, ans: list):
            if n == 0:
                return
            combo = math.factorial(n - 1)
            element = k // combo
            mod = k % combo
            ans += [l[element]]
            l.pop(element)
            rec(mod, n - 1, l, ans)

        l = [i for i in range(1, n + 1)]
        ans = []
        rec(k - 1, n, l, ans)
        return "".join([str(x) for x in ans])


# @leet end

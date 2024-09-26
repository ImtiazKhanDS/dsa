# @leet start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            p = pow(x, n // 2)
            if n % 2 == 0:
                return p * p
            else:
                return x * p * p

        if n < 0:
            return 1 / pow(x, abs(n))
        else:
            return pow(x, n)


# @leet end


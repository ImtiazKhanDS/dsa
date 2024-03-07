# @leet start
from math import sqrt
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(num: int) -> int:
            root, divisor = int(sqrt(num)), 0
            if root * root == num:
                return 0
            for i in range(2, root + 1):
                if not num % i:
                    if divisor:
                        return 0
                    divisor = i
            return num + divisor + num // divisor + 1 if divisor else 0

        return sum(map(divisors, nums))


# @leet end

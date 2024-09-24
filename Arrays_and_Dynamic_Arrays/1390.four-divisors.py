# @leet start
import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            i = 2
            _sum = 0
            _sum = 1 + num
            _count = 0
            res = int(
                math.sqrt(num)
            )  # if the square is perfect then it has odd number of factors so eliminate.
            if res * res == num:
                continue
            while i * i < num:
                if num % i == 0:
                    _sum += i + num / i
                    _count += 1
                    if _count > 1:
                        break
                i += 1

            if _count == 1:
                ans += int(_sum)

        return ans


# @leet end


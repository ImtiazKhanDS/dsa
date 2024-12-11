# @leet start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        _len = 1 << n
        gray_codes = [i ^ (i >> 1) for i in range(_len)]
        return gray_codes


# @leet end

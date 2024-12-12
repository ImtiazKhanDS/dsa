# @leet start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        val1 = 0
        overall_xor = 0
        for n in nums:
            overall_xor ^= n

        least_set_bit = 1

        while not (least_set_bit & overall_xor):
            least_set_bit <<= 1

        for n in nums:
            if least_set_bit & n:
                val1 ^= n
        return val1, overall_xor ^ val1


# @leet end


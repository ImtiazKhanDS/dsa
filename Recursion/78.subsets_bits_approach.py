# @leet start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(2**n):
            bit_repr = f"{i:0{n}b}"
            res = [x if y == "1" else None for x, y in zip(nums, bit_repr)]
            res = [x for x in res if x is not None]
            result.append(res)
        return result


# @leet end

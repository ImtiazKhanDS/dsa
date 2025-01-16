# @leet start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk: list = []
        n = len(nums)
        nge = [-1] * n
        for _ in range(2):
            for i in range(n):
                while stk and nums[stk[-1]] < nums[i]:
                    ele = stk.pop()
                    nge[ele] = nums[i]
                stk.append(i)
        return nge


# @leet end


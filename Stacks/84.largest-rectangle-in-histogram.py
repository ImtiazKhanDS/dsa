# @leet start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = [None] * n
        pse = [None] * n
        stk = []
        stk.append(0)
        for i in range(1, n):
            while stk and heights[stk[-1]] > heights[i]:
                nse[stk[-1]] = i
                stk.pop()
            stk.append(i)
        while stk:
            nse[stk[-1]] = n
            stk.pop()

        stk.append(n - 1)
        for i in range(n - 2, -1, -1):
            while stk and heights[stk[-1]] > heights[i]:
                pse[stk[-1]] = i
                stk.pop()
            stk.append(i)
        while stk:
            pse[stk[-1]] = -1
            stk.pop()

        ans = float("-inf")
        for i in range(n):
            ans = max(ans, heights[i] * (nse[i] - pse[i] - 1))
        return int(ans)


# @leet end


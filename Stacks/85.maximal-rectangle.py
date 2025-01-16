# @leet start
class Solution:

    @staticmethod
    def largestRectangle(heights: List[int]):
        n = len(heights)
        stk: list = []
        max_area = 0
        for i in range(n):
            start = i
            while stk and heights[i] < stk[-1][0]:
                h, j = stk.pop()
                w = i - j
                a = h * w
                max_area = max(max_area, a)
                start = j
            stk.append((heights[i], start))

        while stk:
            h, j = stk.pop()
            w = n - j
            a = h * w
            max_area = max(max_area, a)
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        ans = 0
        for row in matrix:
            for col in range(cols):
                heights[col] = heights[col] + 1 if row[col] == "1" else 0
            ans = max(ans, Solution.largestRectangle(heights))
        return ans


# @leet end


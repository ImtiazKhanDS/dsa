# @leet start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = 0
        ans = []
        while l < n and r < m:
            for temp in range(l, n):
                ans.append(matrix[r][temp])
            r += 1

            for temp in range(r, m):
                ans.append(matrix[temp][n - 1])
            n -= 1

            if r < m:
                for temp in range(n - 1, l - 1, -1):
                    ans.append(matrix[m - 1][temp])
                m -= 1
            if l < n:
                for temp in range(m - 1, r - 1, -1):
                    ans.append(matrix[temp][l])
                l += 1
        return ans


# @leet end

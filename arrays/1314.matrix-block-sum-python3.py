# @leet start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        temp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(1, n):
                mat[i][j] = mat[i][j] + mat[i][j - 1]

        # @leet end
        for j in range(n):
            for i in range(1, m):
                mat[i][j] = mat[i][j] + mat[i - 1][j]

        for i in range(m):
            for j in range(n):
                ans = 0
                i2, j2, i1, j1 = (
                    min(i + k, m - 1),
                    min(j + k, n - 1),
                    max(0, i - k),
                    max(0, j - k),
                )
                ans = mat[i2][j2]
                if i1 > 0 and j1 > 0:
                    ans = ans + mat[i1 - 1][j1 - 1] - mat[i1 - 1][j2] - mat[i2][j1 - 1]
                elif i1 > 0:
                    ans -= mat[i1 - 1][j2]
                elif j1 > 0:
                    ans -= mat[i2][j1 - 1]
                temp[i][j] = ans
        self.answer = temp
        return self.answer


# @leet end

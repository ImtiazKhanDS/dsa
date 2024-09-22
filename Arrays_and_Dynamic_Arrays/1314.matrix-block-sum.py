# @leet start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            _sum = mat[i][0]
            for j in range(1, m):
                _sum += mat[i][j]
                mat[i][j] = _sum

        for j in range(m):
            _sum = mat[0][j]
            for i in range(1, n):
                _sum += mat[i][j]
                mat[i][j] = _sum

        temp = []
        for i in range(n):
            row_res = []
            for j in range(m):
                r2, c2 = min(i + k, n - 1), min(j + k, m - 1)
                ans = mat[r2][c2]
                if i - k > 0:
                    ans -= mat[i - k - 1][c2]
                if j - k > 0:
                    ans -= mat[r2][j - k - 1]
                if i - k > 0 and j - k > 0:
                    ans += mat[i - k - 1][j - k - 1]
                row_res.append(ans)
            temp.append(row_res)
        return temp


# @leet end


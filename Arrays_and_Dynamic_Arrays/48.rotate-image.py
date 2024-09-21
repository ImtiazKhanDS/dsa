# @leet start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose and reverse each row

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print("transposed matrix : ", matrix)
        for i in range(n):
            for j in range(m // 2):
                matrix[i][j], matrix[i][m - j - 1] = matrix[i][m - j - 1], matrix[i][j]
        return matrix


# @leet end


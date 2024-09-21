# @leet start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n = len(self.matrix)
        self.m = len(self.matrix[0])
        print(self.matrix)
        self.matrix_sum = self.get_prefix_sum()

    def get_prefix_sum(self):
        n = self.n
        m = self.m

        matrix = self.matrix.copy()

        for i in range(n):
            _sum = matrix[i][0]
            for j in range(1, m):
                _sum += matrix[i][j]
                matrix[i][j] = _sum

        for j in range(m):
            _sum = matrix[0][j]
            for i in range(1, n):
                _sum += matrix[i][j]
                matrix[i][j] = _sum

        return matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix_sum[row2][col2]
        if row1 > 0:
            ans -= self.matrix_sum[row1 - 1][col2]
        if col1 > 0:
            ans -= self.matrix_sum[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            ans += self.matrix_sum[row1 - 1][col1 - 1]

        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @leet end


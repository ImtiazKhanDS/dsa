# @leet start
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(self.matrix)
        n = len(self.matrix[0])
        for i in range(m):
            print(f"row number {i} : ")
            sum_ = self.matrix[i][0]
            for j in range(1, n):
                self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][j - 1]
        for j in range(n):
            for i in range(1, m):
                self.matrix[i][j] = self.matrix[i][j] + self.matrix[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        else:
            return (
                self.matrix[row2][col2]
                - self.matrix[row1 - 1][col2]
                - self.matrix[row2][col1 - 1]
                + self.matrix[row1 - 1][col1 - 1]
            )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @leet end

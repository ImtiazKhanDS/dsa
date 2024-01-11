# @leet start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose first

        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        # Now reverse each row of the array.
        for k in range(n):
            i = 0
            j = n - 1
            while i < j:
                temp = matrix[k][i]
                matrix[k][i] = matrix[k][j]
                matrix[k][j] = temp
                i += 1
                j -= 1


# @leet end

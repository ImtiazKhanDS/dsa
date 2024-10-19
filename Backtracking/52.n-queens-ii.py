# @leet start
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0 for _ in range(n)] for _ in range(n)]
        count = 0

        def isSafe(i: int, j: int):
            # check column
            for k in range(i, -1, -1):
                if board[k][j] == 1:
                    return False

            # check upward left diagonal
            m = i
            p = j
            while m >= 0 and p >= 0:
                if board[m][p] == 1:
                    return False
                m -= 1
                p -= 1

            # check upward right diagonal
            m = i
            p = j
            while m >= 0 and p < n:
                if board[m][p] == 1:
                    return False
                m -= 1
                p += 1

            return True

        def dfs(i: int):
            nonlocal count
            if i == n:
                count += 1
                return

            for k in range(n):
                if isSafe(i, k):
                    board[i][k] = 1
                    dfs(i + 1)
                    board[i][k] = 0

        dfs(0)
        return count


# @leet end


# @leet start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []

        def isSafe(i: int, j: int):
            # check column
            if i >= n or i < 0 or j < 0 or j >= n:
                return False

            for k in range(i, -1, -1):
                if board[k][j] == "Q":
                    return False

            # check left upward diagonal
            m, k = i, j
            while m >= 0 and k >= 0:
                if board[m][k] == "Q":
                    return False
                m -= 1
                k -= 1

            # check right upward diagonal
            m, k = i, j
            while m >= 0 and k < n:
                if board[m][k] == "Q":
                    return False
                m -= 1
                k += 1

            return True

        def dfs(i: int, j: int):
            if i == n:
                result.append([b.copy() for b in board.copy()])
                return

            for k in range(n):
                if isSafe(i, k):
                    board[i][k] = "Q"
                    dfs(i + 1, k)
                    board[i][k] = "."

        dfs(0, 0)
        final_result = [["".join(e) for e in p] for p in result]
        return final_result


# @leet end


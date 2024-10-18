# @leet start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = set()

        def dfs(r: int, c: int, i: int):
            if i == len(word):
                return True
            if (
                r < 0
                or r >= m
                or c >= n
                or c < 0
                or board[r][c] != word[i]
                or (r, c) in path
            ):
                return False

            path.add((r, c))

            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            path.remove((r, c))
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# @leet end


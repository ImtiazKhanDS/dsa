# @leet start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        st_i, st_j, end_i, end_j, ec = 0, 0, 0, 0, 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    st_i, st_j = i, j
                elif grid[i][j] == 2:
                    end_i, end_j = i, j
                elif grid[i][j] == 0:
                    ec += 1

        def isValidMove(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
                return False
            else:
                return True

        def dfs(i: int, j: int, rem: int):
            if not isValidMove(i, j):
                return 0
            if (i, j) == (end_i, end_j):
                return 1 if rem == 0 else 0

            grid[i][j] = -1
            # traverse right , left, bottom , top
            _sum = (
                dfs(i, j + 1, rem - 1)
                + dfs(i, j - 1, rem - 1)
                + dfs(i + 1, j, rem - 1)
                + dfs(i - 1, j, rem - 1)
            )
            grid[i][j] = 0
            return _sum

        return dfs(st_i, st_j, ec)


# @leet end


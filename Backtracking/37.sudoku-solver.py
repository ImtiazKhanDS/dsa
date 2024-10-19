# @leet start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])
        ans: List = []
        ansfound = False

        # calculate row frequency count

        row_freq = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] != ".":
                    row_freq[i][ord(board[i][j]) - ord("1")] += 1

        # calculate column frequency count

        col_freq = [[0 for _ in range(r)] for _ in range(c)]
        for i in range(c):
            for j in range(r):
                if board[i][j] != ".":
                    col_freq[j][ord(board[i][j]) - ord("1")] += 1

        # calculate 3 * 3 matrices frequency count
        mat_freq = [[0 for _ in range(c)] for _ in range(r)]
        p = -1
        for i in range(0, r, 3):
            for j in range(0, c, 3):
                p += 1
                for m in range(i, i + 3):
                    for k in range(j, j + 3):
                        if board[m][k] == ".":
                            continue
                        else:
                            mat_freq[p][ord(board[m][k]) - ord("1")] += 1

        # print(row_freq, col_freq, mat_freq)

        def getMatNum(i: int, j: int) -> int:
            return (i // 3) * 3 + (j // 3)

        def ss(board: List[List[str]], i: int, j: int):
            nonlocal ansfound
            nonlocal ans
            if ansfound:
                return
            if i == r:
                ansfound = True
                ans.clear()
                for row in board:
                    ans.append(row.copy())
                return

            next_i, next_j = (i, j + 1) if j < 8 else (i + 1, 0)

            if board[i][j] != ".":
                ss(board, next_i, next_j)
                return

            matnum = getMatNum(i, j)

            for val in range(9):
                if (
                    row_freq[i][val] == 0
                    and col_freq[j][val] == 0
                    and mat_freq[matnum][val] == 0
                ):
                    board[i][j] = str(val + 1)
                    row_freq[i][val] += 1
                    col_freq[j][val] += 1
                    mat_freq[matnum][val] += 1

                    ss(board, next_i, next_j)

                    if not ansfound:
                        board[i][j] = "."
                        row_freq[i][val] -= 1
                        col_freq[j][val] -= 1
                        mat_freq[matnum][val] -= 1

        ss(board, 0, 0)
        return ans


# @leet end


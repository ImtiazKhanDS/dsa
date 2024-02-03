# @leet start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            ans = [[1], [1, 1], [1, 2, 1]]
            for i in range(3, numRows):
                ans.append([0] * (i + 1))
                ans[-1][0] = 1
                ans[-1][-1] = 1
                for j in range(1, i):
                    ans[i][j] = ans[i - 1][j] + ans[i - 1][j - 1]
            return ans


# @leet end

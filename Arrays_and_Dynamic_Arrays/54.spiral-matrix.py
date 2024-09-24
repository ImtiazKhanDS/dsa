# @leet start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = m
        u = 0
        d = n
        ans = []
        while l < r and u < d:

            i = l
            while i < r:
                ans.append(matrix[u][i])
                i += 1
            u += 1

            j = u
            while j < d:
                ans.append(matrix[j][r - 1])
                j += 1

            r -= 1

            if not (l < r and u < d):
                break

            i = r - 1
            while i > l - 1:
                ans.append(matrix[d - 1][i])
                i -= 1

            d -= 1

            j = d - 1
            while j > u - 1:
                ans.append(matrix[j][l])
                j -= 1
            l += 1

        return ans


# @leet end


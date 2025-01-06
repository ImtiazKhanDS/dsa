# @leet start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        map: dict = {}
        for i in range(n):
            for j in range(m):
                if not map.get(i + j):
                    map[i + j] = [mat[i][j]]
                else:
                    map[i + j].append(mat[i][j])
        res = []
        for i in range(len(map)):
            if i % 2 == 0:
                res.extend(map[i][::-1])
            else:
                res.extend(map[i])
        return res


# @leet end


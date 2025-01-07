# @leet start
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        map: dict = {}
        r = len(nums)
        for i in range(r):
            c = len(nums[i])
            for j in range(c):
                if not map.get(i + j):
                    map[i + j] = [nums[i][j]]
                else:
                    map[i + j].append(nums[i][j])
        res = []
        for i in range(len(map)):
            res.extend(map.get(i)[::-1])
        return res


# @leet end


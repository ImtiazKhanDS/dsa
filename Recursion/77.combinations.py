# @leet start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(i: int, temp: List):
            if len(temp) == k:
                res.append(temp.copy())
                return

            for p in range(i, n + 1):
                temp.append(p)
                helper(p + 1, temp)
                temp.pop()

        helper(1, [])
        print(res)
        return res


# @leet end


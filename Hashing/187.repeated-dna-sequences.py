# @leet start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        map: dict = {}
        for i in range(0, n - 9):
            map[s[i : i + 10]] = map.get(s[i : i + 10], 0) + 1
        res = [key for key, value in map.items() if value > 1]
        return res


# @leet end


# @leet start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dt = {}
        for i, ch in enumerate(order):
            dt[ch] = i
        s = list(s)
        s.sort(key=lambda x: dt.get(x, 29))
        return "".join(s)


# @leet end


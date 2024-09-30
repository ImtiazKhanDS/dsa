# @leet start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        res = []

        def helper(s: str, i: int):
            if n + 1 == i:
                res.append(s)
                return

            for ch in ["a", "b", "c"]:
                if not s or ch != s[i - 1]:
                    helper(s + ch, i + 1)

        helper(" ", 1)

        print(res, len(res), k)
        if k <= len(res):
            return res[k - 1][1:]
        else:
            return ""


# @leet end


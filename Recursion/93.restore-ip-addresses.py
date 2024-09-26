# @leet start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res: List = []
        n = len(s)
        if n > 12:
            return res  # this is because we can have atmost 3 digits and 4 integers which is 12 digits atmost

        def backtrack(i: int, dots: int, curIP: str):
            if dots == 4 and i == n:
                res.append(curIP[:-1])
                return
            for k in range(i, min(i + 3, n)):
                # single digit allowed zero if its double or triple should not have a leading zero.
                if int(s[i : k + 1]) < 256 and (i == k or s[i] != "0"):
                    backtrack(k + 1, dots + 1, curIP + s[i : k + 1] + ".")

        backtrack(0, 0, "")
        return res


# @leet end


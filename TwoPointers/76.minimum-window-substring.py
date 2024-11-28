# @leet start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if countT.get(c, 0) and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res[0], res[1] = l, r
                    reslen = r - l + 1
                window[s[l]] -= 1
                if countT.get(s[l], 0) and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1]


# @leet end


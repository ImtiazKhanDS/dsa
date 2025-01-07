# @leet start
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patfreq: dict = {}
        for row in matrix:
            T = 0 if row[0] == 0 else 1
            pat = "".join(["T" if r == T else "F" for r in row])
            patfreq[pat] = patfreq.get(pat, 0) + 1
        return max(patfreq.values())


# @leet end


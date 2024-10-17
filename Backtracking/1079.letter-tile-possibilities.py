# @leet start
from collections import defaultdict


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        freq_count = defaultdict(lambda: 0)
        for i in range(n):
            freq_count[tiles[i]] += 1

        def rec():
            res = 0
            for j in freq_count:
                if freq_count[j] > 0:
                    freq_count[j] -= 1
                    res += rec() + 1
                    freq_count[j] += 1
            return res

        return rec()


# @leet end


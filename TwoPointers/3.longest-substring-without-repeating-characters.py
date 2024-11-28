# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if s == "":
            return 0
        i, j = 0, 0
        freq = [0] * 256
        _count = 1
        while j < n:
            if freq[ord(s[j]) - ord("a")] == 0:
                freq[ord(s[j]) - ord("a")] += 1
                j += 1
            else:
                freq[ord(s[i]) - ord("a")] -= 1
                i = i + 1
            _count = max(_count, j - i)
        return _count


# @leet end


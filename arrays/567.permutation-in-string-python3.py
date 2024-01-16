# @leet start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        freq_s1 = [0] * 26
        for i in range(n1):
            freq_s1[ord(s1[i]) - ord("a")] += 1
        freq_s2 = [0] * 26
        for j in range(n1):
            freq_s2[ord(s2[j]) - ord("a")] += 1
        if freq_s1 == freq_s2:
            return True
        for j in range(n1, n2):
            freq_s2[ord(s2[j]) - ord("a")] += 1
            freq_s2[ord(s2[j - n1]) - ord("a")] -= 1
            if freq_s2 == freq_s1:
                return True
        return False


# @leet end

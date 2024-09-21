# @leet start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substr = [0] * 26
        test = [0] * 26

        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            s1, s2 = s2, s1
        for l in s1:
            substr[ord(l) - ord("a")] += 1

        for i in range(s1_len):
            test[ord(s2[i]) - ord("a")] += 1

        if substr == test:
            return True

        for i in range(s1_len, len(s2)):
            test[ord(s2[i - s1_len]) - ord("a")] -= 1
            test[ord(s2[i]) - ord("a")] += 1
            if test == substr:
                return True
        return False


# @leet end


# @leet start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        ans = 0
        n = len(s)
        for i in range(k):
            if s[i] in "aeiou":
                count += 1

        i = k
        j = 0
        ans = max(count, ans)
        while i < n and j < n - k + 1:
            if s[i] in "aeiou":
                count += 1
            if s[j] in "aeiou":
                count -= 1
            i = i + 1
            j = j + 1
            ans = max(ans, count)
        return ans


# @leet end

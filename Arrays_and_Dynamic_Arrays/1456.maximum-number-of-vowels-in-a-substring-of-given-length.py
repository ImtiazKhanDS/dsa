# @leet start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        for i in range(k):
            if s[i] in "aeiou":
                count += 1

        ans = count
        for i in range(k, n):
            if s[i - k] in "aeiou":
                count -= 1
            if s[i] in "aeiou":
                count += 1

            ans = max(count, ans)
        return ans


# @leet end


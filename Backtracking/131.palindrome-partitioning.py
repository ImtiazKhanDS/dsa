## @leet start
class Solution:
    def palindrome(self, st: str, i: int, j: int):
        while i < j:
            if st[i] != st[j]:
                return False
            j -= 1
            i += 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i: int):
            if i >= len(s):
                res.append(part.copy())

            for j in range(i, len(s)):
                if self.palindrome(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res


# @leet end


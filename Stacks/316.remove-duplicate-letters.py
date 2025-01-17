# @leet start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = [0] * 26
        present = [0] * 26
        stk: list = []
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        for ch in s:
            freq[ord(ch) - ord("a")] -= 1
            if present[ord(ch) - ord("a")]:
                continue
            while (
                stk
                and (ord(ch) - ord("a")) < ord(stk[-1]) - ord("a")
                and freq[ord(stk[-1]) - ord("a")] > 0
            ):
                pchar = stk.pop()
                present[ord(pchar) - ord("a")] -= 1
            stk.append(ch)
            present[ord(ch) - ord("a")] += 1
        return "".join(stk)


# @leet end


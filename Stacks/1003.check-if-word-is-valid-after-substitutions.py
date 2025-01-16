# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        stk: list = []
        for ch in s:
            if ch == "c":
                if len(stk) < 2:
                    return False
                else:
                    if stk[-1] == "b" and stk[-2] == "a":
                        stk.pop()
                        stk.pop()
                        continue
            stk.append(ch)
        return len(stk) == 0


# @leet end


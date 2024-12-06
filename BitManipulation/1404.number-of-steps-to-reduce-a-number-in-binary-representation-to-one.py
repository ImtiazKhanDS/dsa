# @leet start
class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        num = int(s, 2)
        mask = 1
        steps = 0
        while num != 1:
            if num & mask:
                num += 1
            else:
                num = num // 2
            steps += 1
        return steps


# @leet end


# @leet start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(l: int, r: int, s: str, n: int):
            if len(s) == 2 * n:
                result.append(s)
                return
            # case 1 : if count('(') == count(')')
            if l == r:
                if l == n and r == n:
                    return
                else:
                    helper(l + 1, r, s + "(", n)
            # case 2 : if count('(') > count(')')
            if l > r:
                if l >= n:
                    helper(l, r + 1, s + ")", n)
                else:
                    helper(l + 1, r, s + "(", n)
                    helper(l, r + 1, s + ")", n)

        st = ""
        helper(0, 0, st, n)
        return result


# @leet end


# @leet start


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        openbraces = ["(", "[", "{"]
        for c in s:
            if c in openbraces:
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                elif c == ")" and not st[-1] == "(":
                    return False
                elif c == "]" and not st[-1] == "[":
                    return False
                elif c == "}" and not st[-1] == "{":
                    return False
                else:
                    st.pop()
        return len(st) == 0


# @leet end


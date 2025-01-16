# @leet start
class Solution:
    def simplifyPath(self, path: str) -> str:
        d = path.split("/")
        d = [i for i in d if i not in ["", "."]]
        new: list = []
        for i in range(len(d)):
            if d[i] == "..":
                if not new:
                    continue
                new.pop()
                continue
            new.append(d[i])
        return "/" + "/".join(new)


# @leet end


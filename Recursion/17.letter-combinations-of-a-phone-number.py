# @leet start
class Solution:
    def __init__(self):
        self.map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.result = []

    def helper(self, digits: str, temp: str, index: int):
        if len(temp) == len(digits):
            self.result.append(temp)
            return

        for letter in self.map[digits[index]]:
            self.helper(digits, temp + letter, index + 1)

    def letterCombinations(self, digits: str) -> List[str]:
        temp = ""
        if len(digits) <= 0:
            return []
        self.helper(digits, temp, 0)
        return self.result


# @leet end


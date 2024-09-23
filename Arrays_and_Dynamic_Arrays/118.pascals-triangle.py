# @leet start
class Solution:

    def __init__(self):
        self.pascal = self.get_pascal()

    def get_pascal(self, n=30):
        pascal = [[0 for _ in range(30)] for _ in range(30)]
        pascal[0][0] = 1
        pascal[1][0] = 1
        pascal[1][1] = 1
        for i in range(2, 30):
            pascal[i][i] = 1
            pascal[i][0] = 1
            for j in range(1, i):
                pascal[i][j] += pascal[i - 1][j] + pascal[i - 1][j - 1]
        return pascal

    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows):
            answer.append([x for x in self.pascal[i] if x != 0])

        return answer


# @leet end


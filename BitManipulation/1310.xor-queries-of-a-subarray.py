# @leet start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        answers = []
        pre_xor = [0] * n

        pre_xor[0] = arr[0]

        for i in range(1, n):
            pre_xor[i] = pre_xor[i - 1] ^ arr[i]

        for left, right in queries:
            ans = pre_xor[right] ^ pre_xor[left - 1] if left else pre_xor[right]
            answers.append(ans)
        return answers


# @leet end


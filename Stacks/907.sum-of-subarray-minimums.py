# @leet start
class Solution:
    @staticmethod
    def get_nse_pse(arr: List[int]):
        n = len(arr)
        nse = [None] * n
        pse = [None] * n
        stk = []
        stk.append(0)
        # calculate next smaller element
        for i in range(1, n):
            while stk and arr[stk[-1]] > arr[i]:
                ele = stk.pop()
                nse[ele] = i
            stk.append(i)
        while stk:
            ele = stk.pop()
            nse[ele] = n
        # calculate previous smaller element
        stk.append(n - 1)
        for i in range(n - 2, -1, -1):
            while stk and arr[stk[-1]] >= arr[i]:
                ele = stk.pop()
                pse[ele] = i
            stk.append(i)
        while stk:
            ele = stk.pop()
            pse[ele] = -1
        ans = 0
        print(nse, pse)
        mod = 10**9 + 7
        for i in range(n):
            l1 = i - pse[i]
            l2 = nse[i] - i
            ans += l1 * l2 * arr[i]
            ans %= mod
        return ans

    def sumSubarrayMins(self, arr: List[int]) -> int:
        return Solution.get_nse_pse(arr)


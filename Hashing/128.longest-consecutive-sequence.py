# @leet start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        mp: dict = {}
        ans = 0
        for n in nums:
            if mp.get(n):
                continue
            else:
                ls, rs = 0, 0
                if mp.get(n - 1):
                    ls = mp.get(n - 1, 0)
                if mp.get(n + 1):
                    rs = mp.get(n + 1, 0)

                mp[n] = 1 + ls + rs
                ans = max(ans, 1 + ls + rs)
                mp[n - ls] = 1 + ls + rs
                mp[n + rs] = 1 + ls + rs
        return ans


# @leet end


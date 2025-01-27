# @leet start
from collections import deque


class Solution:
    def insertAtback(self, d: deque, nums: List[int], i: int):
        while len(d) and nums[d[-1]] < nums[i]:
            d.pop()
        d.append(i)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        d = deque()
        ans = []
        for i in range(k):
            self.insertAtback(d, nums, i)

        for i in range(k, n):
            ans.append(nums[d[0]])
            if d and d[0] == i - k:
                d.popleft()
            self.insertAtback(d, nums, i)
        ans.append(nums[d[0]])
        return ans


# @leet end


# @leet start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        countMap: dict = {}
        left_far, left_near = 0, 0
        for right in range(n):
            countMap[nums[right]] = countMap.get(nums[right], 0) + 1

            while len(countMap) > k:
                countMap[nums[left_near]] -= 1
                if countMap[nums[left_near]] == 0:
                    countMap.pop(nums[left_near])
                left_near += 1
                left_far = left_near

            while countMap.get(nums[left_near], 0) > 1:
                countMap[nums[left_near]] -= 1
                left_near += 1

            if len(countMap) == k:
                res += (left_near - left_far) + 1
        return res


# @leet end


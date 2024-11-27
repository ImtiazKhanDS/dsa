# @leet start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                cursum = nums[i] + nums[left] + nums[right]
                if cursum == target:
                    return target
                if abs(cursum - target) < abs(closest - target):
                    closest = cursum
                if target > cursum:
                    left += 1
                else:
                    right -= 1
        return closest


# @leet end


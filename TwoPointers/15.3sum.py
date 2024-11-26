# @leet start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            rem = -1 * nums[i]
            p1 = i + 1
            p2 = n - 1
            while p1 < p2:
                if nums[p1] + nums[p2] < rem:
                    p1 += 1
                elif nums[p1] + nums[p2] > rem:
                    p2 -= 1
                else:
                    res.append([nums[i], nums[p1], nums[p2]])
                    if nums[p1] == nums[p2]:
                        break
                    else:
                        x, y = nums[p1], nums[p2]
                        while x == nums[p1]:
                            p1 += 1
                        while y == nums[p2]:
                            p2 -= 1
        return res


# @leet end


# @leet start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = [[0, 0], [0, 0]]
        n = len(nums)
        if max(nums) == min(nums):
            return [max(nums)]
        if n <= 2:
            return nums
        for i in range(n):
            if candidates[0][0] == nums[i]:
                candidates[0][1] += 1
            elif candidates[1][0] == nums[i]:
                candidates[1][1] += 1
            elif candidates[0][0] == 0:
                candidates[0][0] = nums[i]
                candidates[0][1] += 1
            elif candidates[1][0] == 0:
                candidates[1][0] = nums[i]
                candidates[1][1] += 1
            else:
                candidates[0][1] -= 1
                candidates[1][1] -= 1
                if candidates[0][1] <= 0:
                    candidates[0][1] = 0
                    candidates[0][0] = 0
                if candidates[1][1] <= 0:
                    candidates[1][0] = 0
                    candidates[1][1] = 0
        answer = []
        print(candidates)
        candidates[0][1] = 0
        candidates[1][1] = 0

        for i in range(n):
            if nums[i] == candidates[0][0]:
                candidates[0][1] += 1
            elif nums[i] == candidates[1][0]:
                candidates[1][1] += 1
        print(candidates)
        for i in range(2):
            if candidates[i][1] > n // 3:
                answer.append(candidates[i][0])
        return answer


# @leet end

# @leet start
class Solution:
    def __init__(self):
        self.subset_list: List = []

    def helper(self, nums: List, index: int, temp: List):
        if index == len(nums):
            self.subset_list.append(temp.copy())
            return temp
        temp.append(nums[index])
        self.helper(nums, index + 1, temp)
        temp.pop()
        self.helper(nums, index + 1, temp)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp: List = []
        self.helper(nums, 0, temp)
        return self.subset_list


# @leet end

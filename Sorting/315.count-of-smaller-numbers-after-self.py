# @leet start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        smaller_arr = [0] * n

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l][1] > right[r][1]:
                    result.append(left[l])
                    # All the elements after rth element will be
                    # smaller than left element since right is arranged
                    # in descending order
                    smaller_arr[left[l][0]] += len(right) - r
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            result.extend(left[l:] or right[r:])
            return result

        indexed_nums = [(i, n) for i, n in enumerate(nums)]
        merge_sort(indexed_nums)
        return smaller_arr


# @leet end


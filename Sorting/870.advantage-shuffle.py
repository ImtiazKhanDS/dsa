# @leet start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        output = [-1] * n
        nums2 = sorted([(v, i) for i, v in enumerate(nums2)])

        l = 0
        r = n - 1
        for i in range(n - 1, -1, -1):
            if nums1[r] > nums2[i][0]:
                output[nums2[i][1]] = nums1[r]
                r -= 1
            else:
                output[nums2[i][1]] = nums1[l]
                l += 1
        return output


# @leet end


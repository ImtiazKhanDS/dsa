# @leet start
class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        first_pairs: dict = {}
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                first_pairs[nums1[i] + nums2[j]] = (
                    first_pairs.get(nums1[i] + nums2[j], 0) + 1
                )
        res = 0
        for i in range(n):
            for j in range(n):
                res += first_pairs.get(-(nums3[i] + nums4[j]), 0)
        return res


# @leet end


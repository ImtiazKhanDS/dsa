# @leet start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        res = []
        while p1 < n1 and p2 < n2:
            if nums1[p1] == nums2[p2]:
                if res and res[-1] == nums1[p1]:
                    pass
                else:
                    res.append(nums1[p1])
                p1 += 1
                p2 += 1
            else:
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1
        return res


# @leet end


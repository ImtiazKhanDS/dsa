# @leet start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def binarysearch(
        self, low: int, high: int, mountain_arr, target: int, invert=False
    ):

        if not invert:
            while low <= high:
                mid = (low + high) // 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        else:
            while low <= high:
                mid = (low + high) // 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) < target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        n = mountain_arr.length()
        l = 0
        h = n - 1
        pivot = 0
        while l <= h:
            m = (l + h) // 2
            if m == 0:
                l = m + 1
            elif m == n - 1:
                h = m - 1
            else:
                left, middle, right = (
                    mountain_arr.get(m - 1),
                    mountain_arr.get(m),
                    mountain_arr.get(m + 1),
                )
                if middle > left and middle > right:
                    pivot = m
                    break
                elif middle < right:
                    l = m + 1
                else:
                    h = m - 1
        res = self.binarysearch(0, pivot, mountain_arr, target)
        if res == -1:
            res = self.binarysearch(pivot + 1, n - 1, mountain_arr, target, True)
        return res


# @leet end


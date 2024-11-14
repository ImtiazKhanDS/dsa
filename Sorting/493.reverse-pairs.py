# @leet start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def inversion_count(arr: list, i: int, j: int):
            nonlocal count
            if i >= j:
                return
            m = (i + j) // 2
            inversion_count(arr, i, m)
            inversion_count(arr, m + 1, j)
            inter_inversion_count(arr, i, m, m + 1, j)

        def inter_inversion_count(arr: list, s1: int, e1: int, s2: int, e2: int):
            nonlocal count
            c = s1
            for j in range(s2, e2 + 1):
                while c <= e1 and arr[c] <= 2 * arr[j]:
                    c += 1
                count += e1 - c + 1

            # Now, merge the two sorted halves to maintain the sorted order
            temp = []
            i, j = s1, s2
            while i <= e1 and j <= e2:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i <= e1:
                temp.append(arr[i])
                i += 1
            while j <= e2:
                temp.append(arr[j])
                j += 1
            for i in range(len(temp)):
                arr[s1 + i] = temp[i]

        inversion_count(nums, 0, len(nums) - 1)
        return count


# @leet end


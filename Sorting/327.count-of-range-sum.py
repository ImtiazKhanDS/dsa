# @leet start


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1] + n)

        def mergesort(left, right):
            if left == right:
                return 0
            mid = (left + right) // 2
            cnt = mergesort(left, mid) + mergesort(mid + 1, right)

            i = j = mid + 1

            for l_ele in cumsum[left : mid + 1]:
                while i <= right and cumsum[i] - l_ele < lower:
                    i += 1
                while j <= right and cumsum[j] - l_ele <= upper:
                    j += 1
                cnt += j - i
            cumsum[left : right + 1] = sorted(cumsum[left : right + 1])
            return cnt

        return mergesort(0, len(cumsum) - 1)


# @leet end


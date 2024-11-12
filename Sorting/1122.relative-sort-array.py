# @leet start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Brute Force
        # dt = {}
        # for i, x in enumerate(arr2):
        #    dt[x] = i

        # arr1.sort()
        # arr1.sort(key = lambda x : dt.get(x, 1001))
        # return arr1

        # count sort
        maxm = max(arr1) + 1
        count = [0] * maxm
        for ele in arr1:
            count[ele] += 1

        result = []
        for value in arr2:
            while count[value] > 0:
                result.append(value)
                count[value] -= 1

        for num in range(maxm):
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result


# @leet end


# @leet start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        def checksorted(num: str):
            nums = [int(p) for p in list(num)]
            firstnum = nums[1]
            temp = []
            for x in range(1, len(nums)):
                temp.append(firstnum + (x - 1))
            return nums[1:] == temp

        def helper(temp: int, i: int):
            if int(temp) >= low and int(temp) <= high and checksorted(temp):
                res.append(int(temp[1:]))

            for k in range(i + 1, 10):
                if checksorted(temp + str(k)):
                    helper(temp + str(k), i + 1)

        helper("0", 0)
        print(res)
        return sorted(res)


# @leet end


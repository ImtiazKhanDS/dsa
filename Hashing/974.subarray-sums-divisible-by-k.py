# @leet start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        psum_mod = 0
        cnt = 0
        mp = {}
        mp[0] = 1
        n = len(nums)
        for i in range(n):
            psum_mod = (psum_mod + nums[i] % k + k) % k
            cnt += mp.get(psum_mod, 0)
            mp[psum_mod] = mp.get(psum_mod, 0) + 1
        return cnt


# @leet end

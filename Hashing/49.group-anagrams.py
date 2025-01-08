# @leet start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp: dict = {}
        for st in strs:
            freq = [0] * 27
            for ch in st:
                if ch != "":
                    freq[ord(ch) - ord("a")] += 1
                else:
                    freq[26] += 1
            freq = "".join(
                str(i) + s for i, s in zip(freq, "abcdefghijklmnopqrstuvwxyz_")
            )
            if mp.get(freq):
                mp[freq].append(st)
            else:
                mp[freq] = [st]
        return list(mp.values())


# @leet end


# @leet start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        str_len = len(s)
        n = len(words)
        word_len = len(words[0])
        word_freq_map: dict = {}
        for word in words:
            word_freq_map[word] = word_freq_map.get(word, 0) + 1
        start_indices = []
        for i in range(str_len - word_len * n + 1):
            tmp_map: dict = {}
            for j in range(i, i + n * word_len, word_len):
                tmp_map[s[j : j + word_len]] = tmp_map.get(s[j : j + word_len], 0) + 1
            if tmp_map == word_freq_map:
                start_indices.append(i)
        return start_indices


# @leet end


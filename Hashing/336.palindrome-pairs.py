# @leet start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reverse_map = {word[::-1]: i for i, word in enumerate(words)}
        result = set()
        for i, word in enumerate(words):
            word_length = len(word)
            # empty case
            if word == "":
                for j, other_word in enumerate(words):
                    if i != j and other_word[::-1] == other_word:
                        result.add((i, j))
                        result.add((j, i))
                continue

            # consider prefixes
            for j in range(word_length + 1):
                prefix, suffix = word[:j], word[j:]

                if (
                    prefix == prefix[::-1]
                    and suffix in reverse_map
                    and reverse_map[suffix] != i
                ):
                    result.add((reverse_map[suffix], i))

                # consider suffixes
                if (
                    suffix == suffix[::-1]
                    and prefix in reverse_map
                    and reverse_map[prefix] != i
                ):
                    result.add((i, reverse_map[prefix]))
        return list(result)


# @leet end


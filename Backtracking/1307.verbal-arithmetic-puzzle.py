# @leet start
from collections import defaultdict


class Solution:
    def isSolvable(self, words, result):
        # sum(words) - result = 0
        def dfs(i, j, path, let2digit, digit2let):
            nonlocal words, m, n

            # base1; traversed all columns
            if j == n:
                return path == 0

            # base2; finished all the row then go to next column at row 0
            # the sum of current column j should be dividable by 10
            if i == m:
                new_path = path // 10  # carry over to next column
                return path % 10 == 0 and dfs(0, j + 1, new_path, let2digit, digit2let)

            # pick the current word in row i
            word = words[i]
            size = len(word)

            # if the prposed j is greater than size, then recur to next row i + 1
            if j >= size:
                return dfs(i + 1, j, path, let2digit, digit2let)

            # read jth letter in word
            ch = word[j]

            # check if it belongs to original words list or it is results
            if i < m - 1:
                sign = 1
            else:
                sign = -1

            # recur to next row i + 1 if ch already has an allocated integer or being the first letter in the word
            if ch in let2digit and (
                let2digit[ch] != 0
                or (let2digit[ch] == 0 and size == 1)
                or j != size - 1
            ):
                new_path = path + sign * let2digit[ch]

                return dfs(i + 1, j, new_path, let2digit, digit2let)

            # we otherwise allocate any possible num= 0, ..., 9 to ch and recur
            for k in range(10):
                # k is not being used before
                if digit2let[k] == "" and (
                    k != 0 or (k == 0 and size == 1) or j != size - 1
                ):

                    # allocate ch and k to maps
                    digit2let[k] = ch
                    let2digit[ch] = k

                    new_path = path + sign * let2digit[ch]

                    # recur dfs with the new_path to the next row
                    if dfs(i + 1, j, new_path, let2digit, digit2let):
                        return True

                    # revert back
                    digit2let[k] = ""
                    if ch in let2digit:
                        del let2digit[ch]

            return False

        # reverse every word as we want to perform sum operations on the map
        words = [word[::-1] for word in words]

        # extend words by adding result to the list
        words += [result[::-1]]

        # total number of words
        m = len(words)

        # total number of columns based on the longest string in words
        n = max(len(word) for word in words)

        let2digit = defaultdict(int)  # stores {ch: digit} s.t. digit = 0, ..., 9
        digit2let = {
            i: "" for i in range(10)
        }  # stores {digit: ch} s.t. digit = 0, ..., 9

        return dfs(0, 0, 0, let2digit, digit2let)

    # @leet end


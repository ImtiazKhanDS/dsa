# Given an integer array of non negative elements
# count the total no of pairs i, j which is divisible by k
from typing import List


def count_pairs_brute_force(arr: List, k: int) -> int:
    m = len(arr)
    count = 0
    for i in range(m):
        for j in range(i + 1, m):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count


def count_pairs(arr: List, k: int) -> int:
    m = len(arr)
    freq = [0] * k
    for i in range(m):
        index = arr[i] % k
        freq[index] += 1
    ans = 0
    ans += freq[0] * (freq[0] - 1) / 2
    for j in range(1, k // 2):
        ans += freq[j] * freq[k - j]
    if k % 2 == 0:
        ans += freq[k // 2] * (freq[(k // 2)] - 1) / 2
    return int(ans)


if __name__ == "__main__":
    arr = [2, 2, 1, 7, 5, 3]
    k = 4
    print(count_pairs_brute_force(arr, k))
    print(count_pairs(arr, k))

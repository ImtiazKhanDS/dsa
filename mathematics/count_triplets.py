# Given a integer array Arr[N] and
# a value m , count of triplets
# i,j,k such that arr[i]+arr[j]+arr[k] divisible by k

from typing import List


def count_triplets(arr: List, m: int):
    rem = [0] * m
    for x in arr:
        rem[x % m] += 1
    ans = 0
    for i in range(m):
        for j in range(i, m):
            k = 0 if (i + j) % m == 0 else m - (i + j) % m
            if k < j:
                continue
            if i == j and j == k:
                ans += int(rem[i] * (rem[i] - 1) * (rem[i] - 2) / 6)
            elif i == j:
                ans += int((rem[i] * (rem[i] - 1) / 2) * rem[k])
            elif i == k:
                ans += int((rem[i] * (rem[i] - 1) / 2) * rem[j])

            elif j == k:
                ans += int((rem[j] * (rem[j] - 1) / 2) * rem[i])

            else:
                ans += rem[i] * rem[j] * rem[k]
    return int(ans)


if __name__ == "__main__":
    arr = [3, 3, 4, 7, 8]
    m = 5
    assert 3 == count_triplets(arr, m)
    assert 4 == count_triplets([3, 3, 3, 3], 3)

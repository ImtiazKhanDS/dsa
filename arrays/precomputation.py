"""Given a integer array N we have
to print the individual sum of q subarrays whose first index
is l and the last index is r is given."""

from typing import List

test = [x for x in range(8)]
queries = [(2, 4), (1, 6)]


def prefix_sum(arr: List):
    n = len(arr)
    prefix_arr = [0] * n
    prefix_arr[0] = arr[0]
    for i in range(1, n):
        prefix_arr[i] = prefix_arr[i - 1] + arr[i]
    return prefix_arr


def answer_queries(prefix_arr: List, queries: List):
    for left, right in queries:
        if left:
            ans = prefix_arr[right] - prefix_arr[left - 1]
        else:
            ans = prefix_arr[right]
        print(ans)


if __name__ == "__main__":
    test = [x for x in range(8)]
    queries = [(2, 4), (1, 6)]
    prefix_arr = prefix_sum(test)
    answer_queries(prefix_arr, queries)
    print("Finished Execution")

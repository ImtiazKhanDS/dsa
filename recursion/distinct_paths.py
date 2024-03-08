# Given a m * n , Find all the distinct paths
# from 0,0 , you are only allowed right
# or down moves.


# Recursion , how many ways to go from
# 0, 0 to m-1, n-1
def countPaths(i: int, j: int) -> int:
    if i == m - 1 or j == n - 1:
        return 1
    return countPaths(i + 1, j) + countPaths(i, j + 1)


# Now changing the way we think about
# recursion here a bit , how many ways
# are there to reach i, j from 0, 0


def countPathAlternate(i: int, j: int) -> int:
    if i == 0 or j == 0:
        return 1
    return countPathAlternate(i - 1, j) + countPathAlternate(i, j - 1)


if __name__ == "__main__":
    m = 3
    n = 3
    print(countPaths(0, 0))
    print(countPathAlternate(m - 1, n - 1))

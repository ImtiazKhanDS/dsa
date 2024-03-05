if __name__ == "__main__":
    n = int(input())
    pascal_triangle = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    pascal_triangle[1][0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if j == 0 or j == i - 1:
                pascal_triangle[i][j] = 1
            else:
                pascal_triangle[i][j] = (
                    pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
                )
    for i in range(1, n + 1):
        for j in range(n + 1):
            print(pascal_triangle[i][j], end=" ")
        print()

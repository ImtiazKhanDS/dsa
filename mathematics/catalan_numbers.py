if __name__ == "__main__":
    n = int(input())
    catalan = [0] * (n + 1)
    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[i - j - 1] * catalan[j]
    print(catalan)

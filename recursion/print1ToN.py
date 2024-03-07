# Given an integer N , print 1 to N using recursion
def print1toN(N):
    if N < 1:
        return
    print1toN(N - 1)
    print(N, end=" ")


def print1toNReverse(N):
    if N < 1:
        return
    print(N, end=" ")
    print1toNReverse(N - 1)


if __name__ == "__main__":
    N = int(input("Enter N : "))
    print1toN(N)
    print("\n Now printing in opposite")
    print1toNReverse(N)

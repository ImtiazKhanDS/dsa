def gcd(a: int, b: int) -> int:
    maxm = max(a, b)
    minm = min(a, b)
    if minm == 0:
        return maxm
    while maxm % minm != 0:
        maxm, minm = minm, maxm % minm
    return minm


if __name__ == "__main__":
    a = int(input("enter a number:"))
    b = int(input("enter another number : "))
    # 1 <= gcd of a,b <= min(a,b)
    print(f"gcd :{gcd(a,b)}")

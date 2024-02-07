from gcd import gcd

# lcm(a,b) = (a*b)/gcd(a,b)


def lcm(a: int, b: int):
    return (a * b) / gcd(a, b)


if __name__ == "__main__":
    a = int(input("enter a number : "))
    b = int(input("enter another number : "))
    print(lcm(a, b))

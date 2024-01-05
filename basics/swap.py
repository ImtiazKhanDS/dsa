"""some blah"""


def swap(x_: int, y_: int):
    """some blah"""
    x_, y_ = y_, x_
    return x_, y_


if __name__ == "__main__":
    x = int(input("Enter x value : "))
    y = int(input("Enter y value : "))
    print(f"The original values of x : {x} and y : {y}")
    x, y = swap(x, y)
    print(f"The swapped values of x : {x} and y : {y}")

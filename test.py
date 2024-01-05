import os
import sys
import time

print(os.path)
print(sys.path)
print(time.time)


print("Hello World ! ")
a = ""


def ab():
    return "working"


def print_list(a: list) -> None:
    print(a)


print_list([1, 2, 3])

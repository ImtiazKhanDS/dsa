class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stk: list = []

    def push(self, x: int) -> None:
        if len(self.stk) < self.maxSize:
            self.stk.append(x)

    def pop(self) -> int:
        if not self.stk:
            return -1
        return self.stk.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stk), k)):
            self.stk[i] += val


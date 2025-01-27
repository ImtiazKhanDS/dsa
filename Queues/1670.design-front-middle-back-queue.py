# @leet start
from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.frontdeque = deque()
        self.backdeque = deque()

    def rebalance(self):
        if len(self.frontdeque) > len(self.backdeque):
            self.backdeque.appendleft(self.frontdeque.pop())
        if len(self.backdeque) > len(self.frontdeque) + 1:
            self.frontdeque.append(self.backdeque.popleft())

    def pushFront(self, val: int) -> None:
        self.frontdeque.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        self.frontdeque.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.backdeque.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if not self.frontdeque and not self.backdeque:
            return -1
        val = self.frontdeque.popleft() if self.frontdeque else self.backdeque.popleft()
        self.rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.frontdeque and not self.backdeque:
            return -1
        if len(self.frontdeque) == len(self.backdeque):
            val = self.frontdeque.pop()
        else:
            val = self.backdeque.popleft()
        self.rebalance()
        return val

    def popBack(self) -> int:
        if not self.frontdeque and not self.backdeque:
            return -1
        if not self.backdeque:
            val = self.frontdeque.popleft()
        else:
            val = self.backdeque.pop()
        self.rebalance()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()# @leet end


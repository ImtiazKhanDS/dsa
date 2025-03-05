# @leet start
class ListNode:
    def __init__(self, val=[0, 0], next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = ListNode((-1, -1))
        self.tail = ListNode((-1, -1))

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]

            # remove the node from current position
            self._remove_node(node)

            # insert node after head
            self._add_to_front(node)

            return node.val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val[1] = value

            self._remove_node(node)
            self._add_to_front(node)
        else:
            if len(self.map) >= self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                self.map.pop(lru_node.val[0])

            # Add the new node
            new_node = ListNode([key, value])
            self.map[key] = new_node
            self._add_to_front(new_node)

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)# @leet end


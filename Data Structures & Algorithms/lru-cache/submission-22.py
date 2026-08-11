class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_map = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1
        else:
            self.remove(self.cache_map[key])
            self.insert(self.cache_map[key])
            return self.cache_map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.remove(self.cache_map[key])

        self.cache_map[key] = Node(key, value)
        self.insert(self.cache_map[key])

        if len(self.cache_map) > self.capacity:
            lru = self.head.next
            print(lru.key)
            self.remove(lru)
            self.cache_map.pop(lru.key)
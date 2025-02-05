class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = Node(-1, -1)  # Dummy head
        self.tail = Node(-1, -1)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self):
        if self.tail.prev == self.head:  # Empty list check
            return None
        removed = self.tail.prev
        self.remove_node(removed)
        return removed

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = Dll()
        self.store = {}

    def get(self, key: int) -> int:
        if key in self.store:
            node = self.store[key]
            self.dll.remove_node(node)
            self.dll.add_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.val = value  # Update value
            self.dll.remove_node(node)
            self.dll.add_head(node)
        else:
            if len(self.store) >= self.capacity:
                removed_node = self.dll.remove_tail()
                del self.store[removed_node.key]  # Always safe

            new_node = Node(key, value)
            self.dll.add_head(new_node)
            self.store[key] = new_node

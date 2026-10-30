class Node:
    def __init__(self, key = None, val = None, prev = None, after = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.after = after

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}

        self.head = Node()
        self.tail = Node()
        self.head.after = self.tail
        self.tail.prev = self.head

    def _unlink(self, key:int):
        tempNode = self.key_map.get(key)
        tempNode.prev.after = tempNode.after
        tempNode.after.prev = tempNode.prev


    def _delete(self, key:int):
        # unlink 
        value = self.key_map.get(key).val
        self._unlink(key)
        del self.key_map[key]
        return key, value
        

    def get(self, key: int) -> int:
        if self.key_map.get(key) == None:
            return -1
        
        # delete existing node
        key, value = self._delete(key)
        # add back in
        self.put(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.key_map.get(key) != None:
            self._delete(key)
            self.put(key,value)
            return

        newNode = Node(key, value)
        self.key_map[key] = newNode
        tempNode = self.head.after
        self.head.after = newNode
        newNode.prev = self.head
        newNode.after = tempNode
        tempNode.prev = newNode

        if len(self.key_map) > self.capacity:
            lru = self.tail.prev
            self._delete(lru.key)
        return
        

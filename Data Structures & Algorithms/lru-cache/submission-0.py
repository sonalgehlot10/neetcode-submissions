class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        #remove the node from the doubly linked list
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self,node):
        #insert the node to the right (MRU) of the doubly linked list and add to the cache
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev, node.next = prev, self.right
        


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key,value)
        self.cache[key] = new_node
        self.insert(new_node)
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

        





















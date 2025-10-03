from collections import deque

"""
Need to keep a deque, with dummy nodes at both ends to enable popping
and rearrangement. We could keep the LRU always to the left most part
of the deque, and the MRU at the right most
So every get operation will pop the element and place to the right
end
And every put, will either update the value else add to right most if 
it doesnt exist else pop and add.

Might need a hashmap to track what exists in the cache and what doesnt
Deque for O(1) get and put operations

Writing my own deque as I need each element to be doubly linked and
I want control over those elements

So to summarize, created a doubly linked list, with key and value in 
each node. Every key will also be stored in a dictionary for fast 
retrieval

Was getting an error due to my custom counting, instead rely on len
of dict function"""

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #for storing each Node. key -> Node
        self.curr_capacity = 0
        self.total_capacity = capacity
        self.leftEnd, self.rightEnd = Node(0, 0), Node(0, 0)
        #Init left and right connected to each other
        self.leftEnd.next = self.rightEnd
        self.rightEnd.prev = self.leftEnd


    def get(self, key: int) -> int:
        #Check if already exists, else -1
        if key not in self.cache: return -1

        #If exists, remove and restitch surrounding indices/Nodes
        val = self.cache[key].val
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return val


    def put(self, key: int, value: int) -> None:
        #Update if already exists
        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key, value)
        self.cache[key] = newNode
        self.add(newNode)

        if len(self.cache) > self.total_capacity:
            lru = self.leftEnd.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def add(self, node):
        prev, nxt = self.rightEnd.prev, self.rightEnd
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
